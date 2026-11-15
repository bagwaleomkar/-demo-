
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 1. Load Dataset
data = pd.read_csv("emails.csv")

# 2. Preprocessing
data = data.drop("Email No.", axis=1)
data = data.dropna()

# 3. Split Features and Target
X = data.drop("Prediction", axis=1)
y = data["Prediction"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Normalize Data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 5. KNN Classification
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

pred1 = knn.predict(X_test)

print("KNN Accuracy:", accuracy_score(y_test, pred1))
print("KNN Confusion Matrix:")
print(confusion_matrix(y_test, pred1))
print(classification_report(y_test, pred1))

# 6. SVM Classification
svm = SVC(kernel='linear')
svm.fit(X_train, y_train)

pred2 = svm.predict(X_test)

print("\nSVM Accuracy:", accuracy_score(y_test, pred2))
print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, pred2))
print(classification_report(y_test, pred2))
