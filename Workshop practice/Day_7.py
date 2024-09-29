#Task 1

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df.head()


#Task 2
from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()

df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(df)

df['Cluster'] = kmeans.labels_

print(df.head())


#task 3
#from sklearn import datasets
#from sklearn.cluster import KMeans
#import pandas as pd
import matplotlib.pyplot as plt

#iris = datasets.load_iris()

#df = pd.DataFrame(data=iris['data'], columns=iris['feature_names'])

#kmeans = KMeans(n_clusters=3, random_state=42)
#kmeans.fit(df[['sepal length (cm)', 'sepal width (cm)']])

#df['Cluster'] = kmeans.labels_

plt.figure(figsize=(10, 8))
plt.scatter(df['sepal length (cm)'], df['sepal width (cm)'], c=df['Cluster'], cmap='viridis', s=50)

#centroids = kmeans.cluster_centers_
#plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')

plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width')
#plt.legend()
plt.show()

#Task 4
