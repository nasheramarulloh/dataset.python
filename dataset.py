# Import library yang diperlukan
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

# Load dataset digits
digits = load_digits()

# Tampilkan bentuk data
print("Shape of data:", digits.data.shape)

# Visualisasi gambar pertama
plt.gray()  # Set warna grayscale
plt.matshow(digits.images[0])  # Menampilkan gambar pertama
plt.title(f"Label: {digits.target[0]}")
plt.show()

# Pisahkan data menjadi fitur (X) dan target (y)
X, y = digits.data, digits.target

# Split data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Inisialisasi model Pohon Keputusan
clf = DecisionTreeClassifier(random_state=42)

# Melatih model
clf.fit(X_train, y_train)

# Prediksi pada data uji
y_pred = clf.predict(X_test)

# Evaluasi model
accuracy = accuracy_score(y_test, y_pred)
print(f"Akurasi model: {accuracy:.2f}")
