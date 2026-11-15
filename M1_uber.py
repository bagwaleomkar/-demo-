# 4. Identify Outliers using Boxplot

plt.figure(figsize=(8, 4))
sns.boxplot(x=data['fare_amount'])
plt.title("Boxplot of Uber Fare Amount")
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

print("Shape after removing outliers:")
print(data.shape)

# Boxplot after removing outliers
plt.figure(figsize=(8, 4))
sns.boxplot(x=data['fare_amount'])
plt.title("Boxplot After Removing Outliers")
plt.show()
