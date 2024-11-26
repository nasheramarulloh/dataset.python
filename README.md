# Dataset load_digits & Algoritma Pohon Keputusan
## Porject Portfolio Exploratory Data Science Python
Dalam dunia Data Science, pohon keputusan adalah salah satu algoritma yang digunakan secara luas untuk tugas klasifikasi dan regresi. Algoritma ini membuat model prediktif dengan membagi data menjadi subset berdasarkan fitur, menyerupai struktur pohon.

Sumber: Artikel GeeksforGeeks: Decision Tree Introduction.

Dataset: Digits Dataset dari Scikit-learn.

Dataset Overview
Dataset digits adalah kumpulan gambar angka tulisan tangan (0-9) yang direpresentasikan sebagai matriks 8x8. Setiap gambar memiliki fitur berupa nilai piksel yang diratakan menjadi vektor berdimensi 64. Tujuannya adalah untuk memprediksi angka dari gambar berdasarkan nilai pikselnya.

**Langkah-langkah Analisis:**
1. Memuat Dataset
Dataset digits akan diakses menggunakan modul datasets dari scikit-learn. Dataset ini memiliki 1.797 sampel data, masing-masing dengan 64 fitur dan target berupa label angka (0–9).
2. Eksplorasi Data
Visualisasi beberapa sampel untuk memahami karakteristik gambar dan distribusi data.
3. Modeling dengan Pohon Keputusan
Membangun model klasifikasi menggunakan DecisionTreeClassifier dari scikit-learn.
4. Evaluasi
Mengukur performa model berdasarkan akurasi pada data uji.

**Hasil Analisis:**
1. Eksplorasi Dataset: Dataset terdiri dari 1.797 sampel, masing-masing dengan 64 fitur.
2. Visualisasi: Gambar angka divisualisasikan menggunakan matplotlib.
3. Klasifikasi dengan Pohon Keputusan:
- Model dilatih dengan data latih (70%) dan diuji pada data uji (30%).
- Akurasi model dihitung untuk mengukur performanya.
4. Matriks Kebingungan: Matriks kebingungan divisualisasikan untuk memahami prediksi yang benar dan salah.
  
**Kesimpulan:**
- Dataset digits adalah kasus ideal untuk pemula dalam klasifikasi multikelas.
- Pohon keputusan, meskipun sederhana, memberikan hasil yang cukup baik untuk dataset kecil.
- Analisis lebih lanjut dapat dilakukan dengan mengoptimalkan parameter seperti max_depth atau mencoba algoritma lain seperti Random Forest atau SVM untuk hasil yang lebih akurat.

Jika Anda memiliki saran atau umpan balik, jangan ragu untuk menghubungi saya melalui:

Email: nasheramarulloh@gmail.com

LinkedIn: Nasher Amarulloh
