# Hasil eksperimen aktual

| Arsitektur | Mode | Best val accuracy | Best epoch | Epoch ≥90% | Waktu training (s) | Parameter dilatih / total | Epoch dijalankan |
|---|---|---:|---:|---:|---:|---:|---:|
| resnet50 | feature | 1.0000 | 2 | 1 | 144.363 | 6147 / 23514179 | 10 |
| resnet50 | partial | 1.0000 | 1 | 1 | 148.486 | 14970883 / 23514179 | 10 |
| resnet50 | scratch | 1.0000 | 5 | 1 | 196.490 | 23514179 / 23514179 | 10 |

Hanya konfigurasi yang memiliki hasil training dicantumkan. Tanda — berarti data tidak tersedia atau ambang belum tercapai.
Angka parameter berasal dari model yang dilatih pada run ini.
Validation berasal dari holdout temporal satu video per kelas, sehingga bukan evaluasi lintas sesi.
