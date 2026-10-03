# Hasil eksperimen aktual

| Arsitektur | Mode | Best val accuracy | Best epoch | Epoch ≥90% | Waktu training (s) | Parameter dilatih / total | Epoch dijalankan |
|---|---|---:|---:|---:|---:|---:|---:|
| mobilenet_v3_small | feature | 1.0000 | 1 | 1 | 16.595 | 592898 / 1519906 | 10 |
| mobilenet_v3_small | partial | 1.0000 | 1 | 1 | 15.549 | 943442 / 1519906 | 10 |
| mobilenet_v3_small | scratch | 0.5000 | 1 | — | 16.120 | 1519906 / 1519906 | 10 |

Hanya konfigurasi yang memiliki hasil training dicantumkan. Tanda — berarti data tidak tersedia atau ambang belum tercapai.
CSV lama tetap dapat dibaca; jumlah parameter dan epoch yang belum dicatat tidak diisi dengan perkiraan.
Validation berasal dari holdout temporal satu video per kelas, sehingga bukan evaluasi lintas sesi.
