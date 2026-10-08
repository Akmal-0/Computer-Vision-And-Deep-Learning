# Desain awal P2 — Earth Block

Tujuan: mengklasifikasikan `red_earth_block`, `blue_earth_block`, dan
`sky_block` dari citra RGB. Dataset saat ini berisi 500 gambar per kelas dan
metadata frame yang diekstrak dari satu video per kelas.

Pipeline memakai ResNet-50 pretrained ImageNet dan membandingkan feature
extraction, fine-tuning parsial, serta training dari awal. Input 224×224,
CrossEntropyLoss, Adam, dan cosine annealing. Perangkat CUDA dipilih otomatis,
dengan fallback CPU.

| Keluaran | Artefak |
|---|---|
| Gambar dan metadata | `dataset/` dan `metadata.csv` |
| Split train/validation | `metadata.csv` setelah `split.py` |
| Checkpoint dan hasil eksperimen | `hasil/models/` dan `hasil/results/` |
| Analisis | `README.md` dan tabel/grafik di folder hasil |

Risiko utama adalah kemiripan frame berurutan dan hanya satu sesi video per
kelas. Split temporal dengan guard band mengurangi kebocoran frame berdekatan,
tetapi evaluasi lintas sesi memerlukan rekaman tambahan.
