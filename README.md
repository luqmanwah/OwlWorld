# OwlWorld

Repositori publik Owl untuk contoh riset AI dan rekayasa sistem yang bisa dijalankan ulang. Contoh di sini berdiri sendiri: tidak memuat data sumber, artefak proyek privat, atau tautan internal.

## Topik

- [Reproduksibilitas cache: kunci gabungan vs. kunci terpisah](topics/cache-reproducibility/demo.py)

Jalankan dari akar repositori:

```sh
python3 topics/cache-reproducibility/demo.py
```

Demo memakai empat permintaan sintetis dan pustaka standar Python saja. Kunci transformasi berisi koordinat sintetis dan versi transformasi. Kunci audit juga memuat versi audit. Baseline menggunakan satu kunci gabungan untuk kedua tahap. Jika hanya versi audit yang berubah, kunci terpisah memungkinkan hasil transformasi dipakai ulang tanpa memakai ulang audit lama.

Ekspektasi yang diperiksa skrip: tiga transformasi pada baseline dan dua pada desain terpisah, dengan tiga audit pada keduanya. Demo menghitung pekerjaan dari kunci unik; tidak menjalankan transformasi geospasial, tidak mengukur latensi, dan bukan bukti kesiapan produksi. Dependensi yang tidak masuk ke kunci tetap dapat menghasilkan cache usang.
