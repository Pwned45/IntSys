# -*- coding: utf-8 -*-
"""lab1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uqmRqQlvaKRiDp6KpSlthjlljPG6crAa
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""# Новый раздел

# Новый раздел
"""

from google.colab import drive
drive.mount('/content/drive')

df = pd.read_csv('drive/MyDrive/ColabNotebooks/housing.csv', sep=" ", encoding='windows-1251', skipinitialspace=True)
df
df.info()

df.rename(columns={'уровень преступности':'CRIM',
                   'удельный вес жилых земель':'ZN',
                   'доля промышленных площадей':'INDUS',
                   'граница с рекой':'CHAS',
                   'концентрация оксидов азота':'NOX',
                   'среднее количество комнат в доме':'RM',
                   'доля домов, построенных до 1940 года':'AGE',
                   'расстояния до бостонских центров занятости':'DIS',
                   'доступность радиальных автомобильных дорог':'RAD',
                   'налога на имущество':'TAX',
                   'Соотношение учеников и учителей':'PTRATIO',
                   '1000(Bk - 0.63)^2':'B',
                   'более низкий статус населения':'LSTAT',
                   'средняя стоимость частных домов':'MEDV'}, inplace=True)
#df.drop('CHAS',axis=1,inplace=True)
df

df

# df['assortment'] = df['assortment'].apply(lambda x: x.strip())
# df['competitor'] = df['competitor'].apply(lambda x: x.strip())
# df['consultant'] = df['consultant'].apply(lambda x: x.strip())
# df['design'] = df['design'].apply(lambda x: x.strip())

# df['assortment'].unique()

# df['competitor'].unique()

# df['consultant'].unique()

# df['design'].unique()

# assortmentDict = {'миним': 0, 'средний': 1, 'широкий': 2, 'макс': 3}
# df['assortment'] = df['assortment'].map(assortmentDict)
# competitorDict = {'хуже': -1, 'одинак': 0, 'лучше': 1}
# df['competitor'] = df['competitor'].map(competitorDict)
# consultantDict = {'Нет': 0, 'Есть': 1}
# df['consultant'] = df['consultant'].map(consultantDict)
# designDict = {'Вывеска': 0, 'Витрина': 1, 'Св+Ви': 2, 'Световая': 3, 'Бедно': 4, 'Вы+Ви': 5}
# df['design'] = df['design'].map(designDict)

dfForX = df.copy()
#dfForX.drop('sales',axis=1,inplace=True)

from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
def graph():
    # df = df.fillna(0)

    m = dfForX.mean(axis=1)
    for i, col in enumerate(dfForX):
        dfForX.iloc[:, i] = dfForX.iloc[:, i].fillna(m)

    # df.head()
    X = dfForX.iloc[:, 1: -1].values
    L = np.array(dfForX.iloc[:, :-1])
    print(L)
    L1 = []
    for i in L:
        L1.append(i[0])
    linked = linkage(X, method='average', metric='euclidean')
    plt.figure(figsize=(13, 13))
    dendrogram(linked, labels=L1)
    # plt.axhline(70, color='r')  # 1.823
    plt.show()
    label = fcluster(linked, 70, criterion='distance')
    np.unique(label)
    dfForX.loc[:, 'label'] = label
    # for i, group in df.groupby('label'):
    #     print(f'cluster {i}')
    #     print(group)
graph()

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

X = dfForX.values[:,:]
X = np.nan_to_num(X)
clust_data = StandardScaler().fit_transform(X)

df = pd.read_csv('drive/MyDrive/ColabNotebooks/housing.csv', sep=" ", encoding='windows-1251', skipinitialspace=True)
#df.drop('CHAS',axis=1,inplace=True)
df.info()

from sklearn.decomposition import PCA
from scipy.spatial.distance import pdist
pca = PCA(2)
df = pca.fit_transform(df)
df.shape
#Initialize the class object
kmeans = KMeans(n_clusters= 3)
 
#predict the labels of clusters.
label = kmeans.fit_predict(df)
 
print(label)
#Getting the Centroids
centroids = kmeans.cluster_centers_
u_labels = np.unique(label)
 
#plotting the results:
 
for i in u_labels:
    plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
plt.scatter(centroids[:,0] , centroids[:,1] , s = 80, color = 'k')
plt.legend()
plt.show()

data_dist = pdist(df, 'euclidean')
data_linkage = linkage(data_dist, method='average')
last = data_linkage[-10:, 0]
last_rev = last[::-1]
idxs = np.arange(1, len(last) + 1)
plt.plot(idxs, last_rev)

acceleration = np.diff(last, 2)  
acceleration_rev = acceleration[::-1]
plt.plot(idxs[:-2] + 1, acceleration_rev)
plt.show()
k = acceleration_rev.argmax() + 2 
print("Рекомендованное количество кластеров:", k)
df_features = pd.read_csv('drive/MyDrive/ColabNotebooks/housing.csv', sep=" ", encoding='windows-1251', skipinitialspace=True)  
 
SSE = [] # хранить сумму квадратов ошибок для каждого результата
for k in range(1,10):
    estimator = KMeans (n_clusters = k) # построить кластер
    estimator.fit(df_features[['CRIM','ZN','INDUS','CHAS','NOX','RM','AGE','DIS','RAD','TAX','PTRATIO','B','LSTAT','MEDV']])
    SSE.append(estimator.inertia_)
X = range(1,10)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X,SSE,'o-')

plt.show()

