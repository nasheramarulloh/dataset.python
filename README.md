# Dataset load_digits & Algoritma Pohon Keputusan
## Porject Portfolio Exploratory Data Science Python
In the world of Data Science, decision trees are one of the algorithms that are widely used for classification and regression tasks. This algorithm creates a predictive model by dividing data into subsets based on features, resembling a tree structure.

Sumber: 
Dataset: https://scikit-learn.org/1.5/modules/generated/sklearn.datasets.load_digits.html#sklearn.datasets.load_digits
Algoritma:https://www.geeksforgeeks.org/decision-tree-introduction-example/

Dataset Overview
The digits dataset is a collection of images of handwritten numbers (0-9) represented as an 8x8 matrix. Each image has features in the form of pixel values ​​which are flattened into a 64-dimensional vector. The goal is to predict numbers from the image based on the pixel values.

**step by step Analisis:**
1. Load Dataset
The digits dataset will be accessed using the datasets module of scikit-learn. This dataset has 1,797 data samples, each with 64 features and targets in the form of number labels (0–9).
2. Data Exploration
Visualization of multiple samples to understand image characteristics and data distribution.
3. Modeling with Decision Trees
1. Load Dataset
The digits dataset will be accessed using the datasets module of scikit-learn. This dataset has 1,797 data samples, each with 64 features and targets in the form of number labels (0–9).
2. Data Exploration
Visualization of multiple samples to understand image characteristics and data distribution.
3. Modeling with Decision Trees
Building a classification model using DecisionTreeClassifier from scikit-learn.
4. Evaluation
Measures model performance based on accuracy on test data.
4. Evaluation
Measures model performance based on accuracy on test data.

**results Analisis:**
1. Dataset Exploration: The dataset consists of 1,797 samples, each with 64 features.
2. Visualization: Figure images are visualized using matplotlib.
3. Classification with Decision Trees:
- The model is trained on training data (70%) and tested on test data (30%).
- Model accuracy is calculated to measure its performance.
4. Confusion Matrix: Confusion matrix is ​​visualized to understand correct and incorrect predictions.
  
**Conclusion:**
- The digits dataset is an ideal case for beginners in multiclass classification.
- Decision trees, although simple, provide quite good results for small datasets.
- Further analysis can be done by optimizing parameters such as max_ depth or trying other algorithms such as Random Forest or SVM for more accurate results.

If you have any suggestions or feedback, please contact me via direct message on LinkedIn or email at:
Email: nasheramarulloh@gmail.com & https://www.linkedin.com/in/nasher-a/
