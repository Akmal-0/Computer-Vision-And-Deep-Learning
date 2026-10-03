# Hasil eksperimen aktual

| Arsitektur | Mode | Best val accuracy | Best epoch | Epoch ≥90% | Waktu training (s) | Parameter dilatih / total | Epoch dijalankan |
|---|---|---:|---:|---:|---:|---:|---:|
| efficientnet_b0 | feature | 1.0000 | 1 | 1 | 16.952 | 2562 / 4010110 | 10 |
| efficientnet_b0 | partial | 1.0000 | 1 | 1 | 17.017 | 1131954 / 4010110 | 10 |
| efficientnet_b0 | scratch | 1.0000 | 8 | 7 | 21.437 | 4010110 / 4010110 | 10 |

Hanya konfigurasi yang memiliki hasil training dicantumkan. Tanda — berarti data tidak tersedia atau ambang belum tercapai.
CSV lama tetap dapat dibaca; jumlah parameter dan epoch yang belum dicatat tidak diisi dengan perkiraan.
Validation berasal dari holdout temporal satu video per kelas, sehingga bukan evaluasi lintas sesi.
