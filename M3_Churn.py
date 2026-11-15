import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, confusion_matrix

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout

# 1. Read Dataset
data = pd.read_csv("Churn_Modelling.csv")

# 2. Explore Dataset
print("First 5 Rows:")
print(data.head())

print("Last 5 Rows:")
print(data.tail())

print("Dataset Shape:")
print(data.shape)

print("Dataset Information:")
data.info()

print("Missing Values:")
print(data.isnull().sum())

print("Statistical Description:")
print(data.describe())

print("Column Names:")
print(data.columns)

# 3. Preprocessing
# axis=1 means columns
data = data.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

# Convert categorical columns into numerical values
data = pd.get_dummies(data, columns=['Geography', 'Gender'], drop_first=True)

# 4. Separate Features and Target
X = data.drop('Exited', axis=1)
y = data['Exited']

# 5. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 6. Normalize Data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# 7. Build Neural Network
model = Sequential()

# input_shape = number of input features
model.add(Dense(16, activation='relu', input_shape=(X_train.shape[1],)))

# Dropout reduces overfitting
model.add(Dropout(0.2))

# Second hidden layer
model.add(Dense(8, activation='relu'))

# Output layer
model.add(Dense(1, activation='sigmoid'))

# 8. Compile Model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# 9. Train Model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# 10. Prediction
pred = model.predict(X_test)
pred = (pred > 0.5).astype(int)

# 11. Evaluation
print("Accuracy:", accuracy_score(y_test, pred) * 100, "%")

print("Confusion Matrix:")
print(confusion_matrix(y_test, pred))
