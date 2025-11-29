# Rod Cutting Problem

## Problem
Diberikan sebuah batang dengan panjang $n$ inci dan sebuah daftar harga $p_i$ untuk $i = 1, 2, \dots, n$. Masalahnya adalah menentukan cara memotong batang tersebut menjadi potongan-potongan yang lebih kecil (atau tidak memotongnya sama sekali) untuk memaksimalkan total pendapatan penjualan.

## Algoritma
Solusi ini menggunakan pendekatan **Dynamic Programming** dengan metode **Bottom-Up**.
- Kita menggunakan array `val` di mana `val[i]` menyimpan pendapatan maksimum yang dapat diperoleh untuk batang dengan panjang `i`.
- Kita menghitung nilai `val[i]` secara berurutan mulai dari $i=1$ hingga $n$.
- Untuk setiap panjang $i$, kita mencari nilai maksimum dengan mencoba memotong batang di posisi $j$ (dari 1 hingga $i$) dan menambahkan harga potongan $p[j]$ dengan nilai optimal dari sisa batang `val[i-j]`.

## Analisis Algoritma
- **Pendekatan**: Dynamic Programming (Bottom-Up).
- **Kompleksitas Waktu**: $O(n^2)$. Hal ini disebabkan oleh dua loop bersarang (nested loop). Loop luar berjalan dari 1 hingga $n$, dan loop dalam berjalan dari 0 hingga $i$.
- **Kompleksitas Ruang**: $O(n)$. Kita menggunakan array tambahan berukuran $n+1$ untuk menyimpan hasil perhitungan sub-masalah.

## Aplikasi/Implementasi
Implementasi algoritma ini dibuat dalam bahasa Python (`rod_cutting.py`). Program menerima daftar harga dan menghitung profit maksimal untuk panjang batang yang sesuai dengan jumlah elemen harga.