
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

# Load dataset
data = pd.read_csv("diabetes.csv")

# Check missing values
print(data.isnull().sum())

# Separate input and output
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# Create KNN model
knn = KNeighborsClassifier(n_neighbors=5)

# Train model
knn.fit(X_train, y_train)

# Predict
knn_pred = knn.predict(X_test)

# Confusion Matrix
cm = confusion_matrix(y_test, knn_pred)
print("Confusion Matrix:\n", cm)

# Accuracy
acc = accuracy_score(y_test, knn_pred)
print("Accuracy:", acc)

# Error Rate
err = 1 - acc
print("Error Rate:", err)

# Precision
precision = precision_score(y_test, knn_pred)
print("Precision:", precision)

# Recall
re = recall_score(y_test, knn_pred)
print("Recall:", re)

# Confusion Matrix Visualization
import seaborn as sns
import matplotlib.pyplot as plt

sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Diabetes Confusion Matrix")
plt.show()
