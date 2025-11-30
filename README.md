# Rod Cutting Problem

## Problem
Diberikan sebuah batang dengan panjang $n$ inci dan sebuah daftar harga $p_i$ untuk $i = 1, 2, \dots, n$. Masalahnya adalah menentukan cara memotong batang tersebut menjadi potongan-potongan yang lebih kecil (atau tidak memotongnya sama sekali) untuk memaksimalkan total pendapatan penjualan.

## Algoritma
Terdapat beberapa pendekatan untuk menyelesaikan masalah ini:

### 1. Naive Recursion
Pendekatan ini memecah masalah menjadi sub-masalah yang lebih kecil secara rekursif tanpa menyimpan hasil perhitungan sebelumnya.
- Untuk setiap panjang batang $n$, kita mencoba memotong di setiap posisi $i$ (dari 1 hingga $n$) dan secara rekursif menghitung nilai maksimum untuk sisa batang $n-i$.
- **File**: `rod_cutting_recursion.py`

### 2. Dynamic Programming - Top Down (Memoization)
Pendekatan ini mirip dengan rekursi, namun menyimpan hasil perhitungan sub-masalah yang sudah diselesaikan dalam tabel (memo) untuk menghindari perhitungan ulang.
- Sebelum menghitung solusi untuk panjang $n$, kita cek apakah nilainya sudah ada di tabel. Jika ada, kembalikan nilai tersebut. Jika belum, hitung dan simpan hasilnya.
- **File**: `rod_cutting_top_down.py`

### 3. Dynamic Programming - Bottom Up (Tabulation)
Pendekatan ini membangun solusi dari masalah terkecil ($i=1$) hingga terbesar ($i=n$) secara iteratif.
- Kita menggunakan array `val` di mana `val[i]` menyimpan pendapatan maksimum untuk batang panjang `i`.
- Nilai `val[i]` dihitung menggunakan nilai-nilai sebelumnya yang sudah diketahui.
- **File**: `rod_cutting_bottom_up.py`


## Analisis Algoritma

### 1. Naive Recursion
- **Kompleksitas Waktu**: $O(2^n)$. Karena banyak sub-masalah yang dihitung berulang kali, pohon rekursi tumbuh secara eksponensial.
- **Kompleksitas Ruang**: $O(n)$ untuk stack rekursi.

### 2. DP Top Down (Memoization)
- **Kompleksitas Waktu**: $O(n^2)$. Setiap sub-masalah hanya dihitung sekali. Terdapat $n$ sub-masalah, dan masing-masing membutuhkan loop $O(n)$ untuk mencari potongan optimal.
- **Kompleksitas Ruang**: $O(n)$ untuk tabel memo dan stack rekursi.

### 3. DP Bottom Up
- **Kompleksitas Waktu**: $O(n^2)$. Terdapat dua loop bersarang. Loop luar berjalan $n$ kali, dan loop dalam rata-rata $n/2$ kali.
- **Kompleksitas Ruang**: $O(n)$ untuk array tabel DP.


## Aplikasi/Implementasi
Implementasi algoritma tersedia dalam empat file Python yang berbeda sesuai pendekatan di atas.
Masalah Rod Cutting memiliki berbagai aplikasi di dunia nyata, terutama dalam bidang manufaktur dan optimasi sumber daya:

1.  **Industri Manufaktur (Cutting Stock Problem)**:
    Digunakan untuk memotong bahan baku panjang (seperti pipa baja, balok kayu, gulungan kertas, atau kain) menjadi ukuran-ukuran standar yang dipesan pelanggan untuk meminimalkan sisa bahan (limbah) atau memaksimalkan keuntungan penjualan.

2.  **Alokasi Sumber Daya**:
    Dapat diterapkan dalam membagi sumber daya yang terbatas (seperti waktu server, bandwidth, atau anggaran iklan) ke dalam unit-unit yang lebih kecil yang memiliki nilai atau prioritas berbeda untuk memaksimalkan total utilitas.

3.  **Strategi Penjualan (Bundling)**:
    Menentukan kombinasi paket produk terbaik untuk dijual. Misalnya, menjual barang dalam satuan, lusinan, atau grosir, di mana setiap ukuran paket memiliki margin keuntungan yang berbeda.