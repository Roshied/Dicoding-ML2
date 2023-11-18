# Laporan Proyek Machine Learning Roshied Mohammad

Sebelum bepergian, biasanya seseorang akan membuat rencana terlebih dahulu tentang lokasi yang akan dikunjungi dan waktu keberangkatan (Asmara, 2019). Hal ini dilakukan untuk menghindari masalah, salah satunya adalah jarak yang akan ditempuh dan waktu yang dibutuhkan tidak sesuai dengan harapan.

Meskipun Indonesia memiliki tempat-tempat yang menarik untuk pariwisata - pedalaman yang indah, reruntuhan budaya dan sejarah yang menarik, pantai, kehidupan malam (Jakarta dan Bali), dan banyak lagi - negara ini gagal menarik banyak turis asing (Dwitama, 2018). Memang benar bahwa Indonesia dapat mencapai targetnya untuk menyambut 10 juta wisatawan mancanegara pada tahun 2015, tetapi angka ini jauh lebih rendah daripada jumlah wisatawan yang berkunjung ke negara tetangga.

Pada proyek ini dibuat sistem rekomendasi Tourism Indonesia, yang bertujuan untuk membantu turis menentukan pilihannya untuk menemukan liburan yang paling cocok untuk turis tersebut. Indonesia menjadi tempat yang sering dikunjungi oleh turis menjadikan faktor utama dibutuhkannya sistem rekomendasi. Yang nantinya dapat membantu turis mengatahui informasi-informasi mengenai tempat liburan yang direkomendasi.

## Project Overview

## Business Understanding
### Problem Statement
- Bagaiamana sistem rekomendasi yang baik untuk proyek sistem rekomendasi ini?
- Bagaimana cara membuat sistem rekomendasi untuk Tourism Indonesia?
### Goals
- Mengetahui sistem rekomendasi yang baik untuk proyek sistem rekomendasi.
- Mengetahui cara membuat sistem rekomendasi untuk Tourism Indonesia.
### Solution Statement
- Pada data preparation melakukan pembersihan data duplikasi
- Pada data preparation memberikan visualisasi data untuk data numerik
- Menggunakan Content-Based Filtering
## Data Understanding
Pada repository ini digunakan dataset [Indonesia Tourism](https://www.kaggle.com/datasets/aprabowo/indonesia-tourism-destination?select=package_tourism.csv). Data ini memiliki 437 Tempat wisata dengan 300 pengguna yang memberikan rating pada tempat wisata tersebut.
### Data Loading
Memunculkan dataframe-dataframe dari dataset.

Tabel 1. data id
|index|Place\_Id|Place\_Name|Description|Category|City|Price|Rating|Time\_Minutes|Coordinate|Lat|Long|
|---|---|---|---|---|---|---|---|---|---|---|---|
|0|1|Monumen Nasional|Monumen Nasional atau yang populer disingkat dengan Monas atau Tugu Monas adalah monumen peringatan setinggi 132 meter \(433 kaki\) yang didirikan untuk mengenang perlawanan dan perjuangan rakyat Indonesia untuk merebut kemerdekaan dari pemerintahan kolonial Hindia Belanda\. Pembangunan monumen ini dimulai pada tanggal 17 Agustus 1961 di bawah perintah presiden Soekarno dan dibuka untuk umum pada tanggal 12 Juli 1975\. Tugu ini dimahkotai lidah api yang dilapisi lembaran emas yang melambangkan semangat perjuangan yang menyala-nyala\. Monumen Nasional terletak tepat di tengah Lapangan Medan Merdeka, Jakarta Pusat\.|Budaya|Jakarta|20000|4\.6|15\.0|\{'lat': -6\.1753924, 'lng': 106\.8271528\}|-6\.1753924|106\.8271528|
|1|2|Kota Tua|Kota tua di Jakarta, yang juga bernama Kota Tua, berpusat di Alun-Alun Fatahillah, yaitu alun-alun yang ramai dengan pertunjukan rutin tarian tradisional\. Museum Sejarah Jakarta adalah bangunan era Belanda dengan lukisan dan barang antik, sedangkan Museum Wayang memamerkan boneka kayu khas Jawa\. Desa Glodok, atau Chinatown, terkenal dengan makanan kaki lima, seperti pangsit dan mi goreng\. Di dekatnya, terdapat sekunar dan kapal penangkap ikan di pelabuhan Sunda Kelapa yang kuno|Budaya|Jakarta|0|4\.6|90\.0|\{'lat': -6\.137644799999999, 'lng': 106\.8171245\}|-6\.1376448|106\.8171245|
|2|3|Dunia Fantasi|Dunia Fantasi atau disebut juga Dufan adalah tempat hiburan yang terletak di kawasan Taman Impian Jaya Ancol, Jakarta Utara, Indonesia\. Dufan diresmikan dan dibuka pada tanggal 29 Agustus 1985\.|Taman Hiburan|Jakarta|270000|4\.6|360\.0|\{'lat': -6\.125312399999999, 'lng': 106\.8335377\}|-6\.1253124|106\.8335377|
|3|4|Taman Mini Indonesia Indah \(TMII\)|Taman Mini Indonesia Indah merupakan suatu kawasan taman wisata bertema budaya Indonesia di Jakarta Timur\. Area seluas kurang lebih 150 hektare atau 1,5 kilometer persegi ini terletak pada koordinat 6°18′6\.8″LS,106°53′47\.2″BT|Taman Hiburan|Jakarta|10000|4\.5|NaN|\{'lat': -6\.302445899999999, 'lng': 106\.8951559\}|-6\.3024459|106\.8951559|
|4|5|Atlantis Water Adventure|Atlantis Water Adventure atau dikenal dengan Atlantis Ancol akan menyuguhkan petualangan wisata air tak terlupakan\. Tempat Wisata bertemakan permainan air dengan luas 5 hektar ini memberi sensasi petualangan di 8 kolam utama\. Yaitu kolam Antila, Plaza Atlas, Poseidon, Aquarius, Octopus, Kiddy Pool, dan Atlantean\. Berlokasi di kawasan Ancol Jakarta Baycity, Atlantis bisa menjadi pilihan destinasi yang pas untuk wisata berenang\.|Taman Hiburan|Jakarta|94000|4\.5|60\.0|\{'lat': -6\.12419, 'lng': 106\.839134\}|-6\.12419|106\.839134|

Tabel 2. info data id
| #   | Column        | Non-Null Count | Dtype   |
|-----|---------------|-----------------|---------|
| 0   | Place_Id      | 437 non-null    | int64   |
| 1   | Place_Name    | 437 non-null    | object  |
| 2   | Description   | 437 non-null    | object  |
| 3   | Category      | 437 non-null    | object  |
| 4   | City          | 437 non-null    | object  |
| 5   | Price         | 437 non-null    | int64   |
| 6   | Rating        | 437 non-null    | float64 |
| 7   | Time_Minutes  | 205 non-null    | float64 |
| 8   | Coordinate    | 437 non-null    | object  |
| 9   | Lat           | 437 non-null    | float64 |
| 10  | Long          | 437 non-null    | float64 |

Tabel 3. data rating
|index|User\_Id|Place\_Id|Place\_Ratings|
|---|---|---|---|
|0|1|179|3|
|1|1|344|2|
|2|1|5|5|
|3|1|373|3|
|4|1|101|4|


Tabel 4. info data rating

| #   | Column        | Non-Null Count | Dtype |
|-----|---------------|-----------------|-------|
| 0   | User_Id       | 10000 non-null | int64 |
| 1   | Place_Id      | 10000 non-null | int64 |
| 2   | Place_Ratings | 10000 non-null | int64 |

Tabel 5. data user
|index|User\_Id|Location|Age|
|---|---|---|---|
|0|1|Semarang, Jawa Tengah|20|
|1|2|Bekasi, Jawa Barat|21|
|2|3|Cirebon, Jawa Barat|23|
|3|4|Bekasi, Jawa Barat|21|
|4|5|Lampung, Sumatera Selatan|20|

Tabel 6. info data users
| #   | Column    | Non-Null Count | Dtype  |
|-----|-----------|-----------------|--------|
| 0   | User_Id   | 300 non-null    | int64  |
| 1   | Location  | 300 non-null    | object |
| 2   | Age       | 300 non-null    | int64  |

### Visualisasi Data
dataframe pada tourism_rating dan tourism_with_id disatukan menjadi
Tabel 7. Data yang telah disatukan
|index|User\_Id|Place\_Id|Place\_Ratings|Place\_Name|City|Category|
|---|---|---|---|---|---|---|
|0|1|179|3|Candi Ratu Boko|Yogyakarta|Budaya|
|1|1|344|2|Pantai Marina|Semarang|Bahari|
|2|1|5|5|Atlantis Water Adventure|Jakarta|Taman Hiburan|
|3|1|373|3|Museum Kereta Ambarawa|Semarang|Budaya|
|4|1|101|4|Kampung Wisata Sosro Menduran|Yogyakarta|Budaya|

Kemudian dibentuk grafik jumlah tiap-tiap fitur numerik seperti categort, city, dan rating
- Grafik Category
  
![image](https://github.com/Roshied/Dicoding-ML2/assets/68040731/f0db0242-1c5e-44b8-a362-c8e52b0f68f4)

Gambar 1. grafik jumlah category pada data
- Grafik City

![image](https://github.com/Roshied/Dicoding-ML2/assets/68040731/7fc1559f-a323-4b22-9718-1137b5db56f8)

Gambar 2. grafik jumlah city pada data
- Grafik rating

![image](https://github.com/Roshied/Dicoding-ML2/assets/68040731/0cc0e3c2-1191-4f91-920c-a25933ae8aab)

Gambar 3. grafik jumlah rating pada data

## Data Preparation
### Missing Value
Setelah proses penggabungan, dilakukan pengecekan terhadap data yang memiliki missing value. Pengecekan missing value dilakukan untuk mengidentifikasi apakah terdapat nilai-nilai yang hilang atau tidak lengkap dalam dataset. Missing value dapat muncul karena berbagai alasan seperti kesalahan input. Menghapus missing value dapat membantu mengurangi error dalam pemodelan nantinya.
### Duplicate
Selanjutnya, Data yang digunakan adalah data unik yang dimasukkan ke dalam proses pemodelan. Oleh karena itu, penghapusan data yang duplikat dengan fungsi **drop_duplicates()**.
Tabel 8. Data tanpa duplicate
|index|User\_Id|Place\_Id|Place\_Ratings|Place\_Name|City|Category|
|---|---|---|---|---|---|---|
|0|1|179|3|Candi Ratu Boko|Yogyakarta|Budaya|
|1|1|344|2|Pantai Marina|Semarang|Bahari|
|2|1|5|5|Atlantis Water Adventure|Jakarta|Taman Hiburan|
|3|1|373|3|Museum Kereta Ambarawa|Semarang|Budaya|
|4|1|101|4|Kampung Wisata Sosro Menduran|Yogyakarta|Budaya|
### Konversi data menjadi list
Tabel 9. Konversi menjadi list
|index|user\_id|place\_id|place\_ratings|place\_name|city|category|
|---|---|---|---|---|---|---|
|0|1|179|3|Candi Ratu Boko|Yogyakarta|Budaya|
|1|1|344|2|Pantai Marina|Semarang|Bahari|
|2|1|5|5|Atlantis Water Adventure|Jakarta|Taman Hiburan|
|3|1|373|3|Museum Kereta Ambarawa|Semarang|Budaya|
|4|1|101|4|Kampung Wisata Sosro Menduran|Yogyakarta|Budaya|
## TF-IDF Vectorizer
Pada tahap ini, membangun sistem rekomendasi sederhana berdasarkan category dari tempat tourism. Teknik ini digunakan pada sistem rekomendasi untuk menemukan representasi fitur penting dari setiap kategori.
## Modeling and Result
Setelah dilakukkan data preparation, dilakukan pemodelan dengan menggunakan cosine similarity.
### Cosine Similarity
Cosine similarity adalah metrik kemiripan yang digunakan untuk mengukur sejauh mana dua vektor berada dalam arah yang sama dalam ruang berdimensi banyak. Ini sering digunakan dalam pengolahan teks dan analisis dokumen, tetapi juga dapat diterapkan pada berbagai bidang lain.
Cosine similarity mengukur kedekatan antara dua vektor dengan mengukur kosinus sudut antara mereka. Nilai cosine similarity berkisar antara -1 dan 1, di mana nilai 1 menunjukkan kedua vektor sepenuhnya sejajar, nilai -1 menunjukkan kedua vektor sejajar tetapi berlawanan arah, dan nilai 0 menunjukkan bahwa kedua vektor tegak lurus satu sama lain.

$$
\[ \text{Cosine Similarity}(A, B) = \frac{A \cdot B}{\|A\| \cdot \|B\|} \]
$$

## Evaluation
Pada evaluasi metrik yang digunakan pada model cosine similarity adalah dengan mengevaluasi presisi (precision), recall, dan F1-score untuk matriks kemiripan biner. Metrik-metrik ini umumnya digunakan dalam masalah klasifikasi biner, dan mereka mengevaluasi kinerja model dalam hal prediksi benar positif (TP), salah positif (FP), salah negatif (FN), dan benar negatif (TN).
dengan output:

Tabel 10. Metrik evaluasi cosine similarity
|   | Precision | Recall | F1-Score |
|---|-----------|--------|----------|
| 0 | 1.0       | 1.0    | 1.0      |
| 1 | 1.0       | 1.0    | 1.0      |
| 2 | 1.0       | 1.0    | 1.0      |
| 3 | 1.0       | 1.0    | 1.0      |
| 4 | 1.0       | 1.0    | 1.0      |
|...| ...       | ...    | ...      |
| 432 | 1.0     | 1.0    | 1.0      |
| 433 | 1.0     | 1.0    | 1.0      |
| 434 | 1.0     | 1.0    | 1.0      |
| 435 | 1.0     | 1.0    | 1.0      |
| 436 | 1.0     | 1.0    | 1.0      |

## Reference
Dwitama, E. (2018). PENGEMBANGAN OBJEK WISATA DANAU LINTING SEBAGAI DAYA TARIK WISATA DI KABUPATEN DELI SERDANG SUMATERA UTARA PENGEMBANGAN OBJEK WISATA DANAU LINTING SEBAGAI DAYA TARIK WISATA DI KABUPATEN DELI SERDANG SUMATERA UTARA (Doctoral dissertation, Sekolah Tinggi Pariwisata Ambarrukmo (STIPRAM) Yogyakarta).
Asmara, R., Prasetyaningrum, I., & Rahmawati, S. Z. (2019). Penyusunan Itinerary Otomatis Tempat Wisata Jatim Menggunakan Google Maps Dan Multitransportasi. INOVTEK Polbeng-Seri Informatika, 4(2), 179-192.
