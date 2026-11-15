
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

# 1. Read Dataset
data = pd.read_csv("uber.csv")

# 2. Explore Dataset
print("First 5 Rows:")
print(data.head())

print("\nDataset Shape:")
print(data.shape)

print("\nDataset Information:")
data.info()

print("\nMissing Values:")
print(data.isnull().sum())

print("\nStatistical Description:")
print(data.describe())

print("\nColumn Names:")
print(data.columns)

# 3. Preprocessing
data = data.dropna()
data = data.drop_duplicates()

# Remove unnecessary columns
data = data.drop(['Unnamed: 0', 'key'], axis=1, errors='ignore')

# Convert pickup_datetime into datetime format
data['pickup_datetime'] = pd.to_datetime(data['pickup_datetime'])

# Extract pickup hour
data['hour'] = data['pickup_datetime'].dt.hour

# Remove original datetime column
data = data.drop('pickup_datetime', axis=1)

# 4. Boxplot Before Removing Outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x=data['fare_amount'])
plt.title("Boxplot Before Removing Outliers")
plt.show()

# 5. Remove Outliers using IQR
Q1 = data['fare_amount'].quantile(0.25)
Q3 = data['fare_amount'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

data = data[
    (data['fare_amount'] >= lower) &
    (data['fare_amount'] <= upper)
]

print("\nShape after removing outliers:")
print(data.shape)

# 6. Boxplot After Removing Outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x=data['fare_amount'])
plt.title("Boxplot After Removing Outliers")
plt.show()

# 7. Correlation Heatmap
print("\nCorrelation:")
print(data.corr(numeric_only=True))

sns.heatmap(data.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

# 8. Separate Features and Target
X = data.drop('fare_amount', axis=1)
y = data['fare_amount']

# 9. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 10. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

pred1 = lr.predict(X_test)

# 11. Random Forest Regression
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

pred2 = rf.predict(X_test)

# 12. Evaluate Models
print("\nLinear Regression Results")
print("R2 Score:", r2_score(y_test, pred1))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred1)))
print("MAE:", mean_absolute_error(y_test, pred1))

print("\nRandom Forest Results")
print("R2 Score:", r2_score(y_test, pred2))
print("RMSE:", np.sqrt(mean_squared_error(y_test, pred2)))
print("MAE:", mean_absolute_error(y_test, pred2))
