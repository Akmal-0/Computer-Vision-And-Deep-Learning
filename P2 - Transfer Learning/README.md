# P2 — Transfer Learning untuk Earth Block

Klasifikasi tiga kelas: `red_earth_block`, `blue_earth_block`, dan `sky_block`.
Dataset aktif berisi 500 gambar per kelas yang diekstrak dari satu video untuk
masing-masing kelas.

## Dataset dan pembagian

Jalankan `python3 prepare_dataset.py` untuk membuat `metadata.csv` dari
`dataset/{Red_Earth_Block,Blue_Earth_Block,Sky_Block}`. Skrip mencocokkan
daftar frame dengan gambar dan `extraction.json`, memvalidasi gambar, serta
mengambil label dari nama folder. Lalu jalankan `python3 split.py`.

Split menahan 20% bagian akhir urutan frame tiap kelas dan mengeluarkan dua
sampel di sekitar batas sebagai guard band. Dengan data saat ini, tiap kelas
memiliki 398 train, 98 validation, dan 4 excluded. Karena setiap kelas berasal
dari satu video, validation ini belum mengukur generalisasi ke sesi pengambilan
yang berbeda. Gunakan beberapa sesi per kelas untuk evaluasi lintas sesi.

## Eksperimen

Konfigurasi mengikuti pipeline P2: ResNet-50, input RGB 224×224, normalisasi
ImageNet, 10 epoch, batch 16, seed 42, Adam, dan CosineAnnealingLR. Data train
menggunakan RandomResizedCrop, HorizontalFlip, dan ColorJitter. Validation
menggunakan resize dan center crop deterministik.

| Mode | Bobot awal | Bagian yang dilatih | Learning rate |
|---|---|---|---|
| feature | ImageNet | classifier; backbone beku | 1e-3 |
| partial | ImageNet | layer4 dan classifier | layer4 1e-4, classifier 1e-3 |
| scratch | acak | seluruh model | 1e-3 |

### Hasil training aktual

| Mode | Best validation accuracy | Epoch terbaik | Epoch pertama ≥90% | Waktu training (s) | Parameter dilatih |
|---|---:|---:|---:|---:|---:|
| feature | 100.00% | 2 | 1 | 144.363 | 6.147 |
| partial | 100.00% | 1 | 1 | 148.486 | 14.970.883 |
| scratch | 100.00% | 5 | 1 | 196.490 | 23.514.179 |

Semua mode mencapai 100% pada holdout temporal ini. Scratch sempat turun ke
90.14% di epoch 4 sebelum mencapai 100% di epoch 5. Validation berisi 294
gambar; hasil ini belum menunjukkan akurasi pada sesi video yang berbeda.

Hasil aktual: [tabel eksperimen](hasil/results/experiments.md),
[akurasi per epoch](hasil/results/accuracy_per_epoch.png), dan
kurva [feature](hasil/results/feature_curves.png),
[partial](hasil/results/partial_curves.png),
[scratch](hasil/results/scratch_curves.png).

Training dijalankan pada CUDA, NVIDIA GeForce RTX 4050 Laptop GPU, PyTorch
2.14.0+cu130.

Latency batch 1 dicatat di
[CSV](hasil/results/latency.csv) dan diringkas dalam
[tabel latency](hasil/results/latency_summary.md) serta
[grafik](hasil/results/latency_bar.png). Pengukuran hanya mencakup
forward pass PyTorch, bukan kamera, preprocessing, postprocessing, atau ROS2.
Target slide 16 adalah anggaran inferensi 35 ms dari sekitar 67 ms per frame
pada 15 FPS; hasil laptop tidak membuktikan performa pada komputer robot.

| Mode | Median (ms) | Mean (ms) | P95 (ms) |
|---|---:|---:|---:|
| feature | 3.200 | 3.015 | 3.238 |
| partial | 2.793 | 2.777 | 2.828 |
| scratch | 2.818 | 2.828 | 2.888 |

## Menjalankan

```bash
python3 prepare_dataset.py
python3 split.py
python3 train.py --epochs 10 --batch-size 16 --seed 42
python3 latency.py --mode all --image dataset/Red_Earth_Block/Red_Earth_Block__frame_000000000.jpg
```

Checkpoint dan semua hasil run baru disimpan di `hasil/` agar
terpisah dari folder kode dan dataset aktif. CUDA dipakai otomatis bila
tersedia; jika tidak, training berjalan di CPU.
