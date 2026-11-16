
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.metrics import silhouette_score

# Load dataset
df = pd.read_csv("sales_data_sample.csv", encoding="latin1")

print(df.head())

# Select numerical columns
X = df[['QUANTITYORDERED', 'PRICEEACH', 'SALES', 'MSRP']]

# Scale data
sc = StandardScaler()
X = sc.fit_transform(X)

# Elbow Method
wcss = []

for i in range(1, 11):
    model = KMeans(n_clusters=i, random_state=42, n_init=10)
    model.fit(X)
    wcss.append(model.inertia_)

# Plot Elbow Graph
plt.plot(range(1, 11), wcss, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.title("Elbow Method")
plt.show()

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
y_kmeans = kmeans.fit_predict(X)

print("K-Means Silhouette Score:", silhouette_score(X, y_kmeans))
print("K-Means Clusters:", y_kmeans[:10])

# Hierarchical Clustering
hc = AgglomerativeClustering(n_clusters=3)
y_hc = hc.fit_predict(X)

print("Hierarchical Silhouette Score:", silhouette_score(X, y_hc))
print("Hierarchical Clusters:", y_hc[:10])
