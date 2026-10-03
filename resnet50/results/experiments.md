# Hasil eksperimen aktual

| Arsitektur | Mode | Best val accuracy | Best epoch | Epoch ≥90% | Waktu training (s) | Parameter dilatih / total | Epoch dijalankan |
|---|---|---:|---:|---:|---:|---:|---:|
| resnet50 | feature | 1.0000 | 1 | 1 | 19.462 | 4098 / 23512130 | 10 |
| resnet50 | partial | 1.0000 | 1 | 1 | 20.573 | 14968834 / 23512130 | 10 |
| resnet50 | scratch | 1.0000 | 2 | 2 | 27.293 | 23512130 / 23512130 | 10 |

Hanya konfigurasi yang memiliki hasil training dicantumkan. Tanda — berarti data tidak tersedia atau ambang belum tercapai.
CSV lama tetap dapat dibaca; jumlah parameter dan epoch yang belum dicatat tidak diisi dengan perkiraan.
Validation berasal dari holdout temporal satu video per kelas, sehingga bukan evaluasi lintas sesi.
