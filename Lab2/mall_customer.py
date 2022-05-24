#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 20:34:21 2021

@author: muratbuyukbas
"""

#SOM ile otomatik kümeleme

import pandas as pd
import SimpSOM as sps
from sklearn.cluster import KMeans
import numpy as np
from sklearn.preprocessing import LabelEncoder



veri = pd.read_csv("Mall_Customers.csv")
X = veri.drop(["CustomerID", "Age"], axis=1)
le = LabelEncoder()
X["Genre"] = le.fit_transform(X["Genre"])




#Ağ oluşturma
net = sps.somNet(20, 20, X.values)

#Ağ eğitimi
net.train(0.01, 1000)

#Veri noktalarının 2 boyutlu bir haritaya gömmek ve kümelemek
hrt = np.array((net.project(X.values)))
kort = KMeans(n_clusters=4, max_iter=300, random_state = 0)

#Örneklerin hangi kümelere ait olduğunu belirlemek
y_ort = kort.fit_predict(hrt)

#Kümeleri etiketlemek
veri["kümeler"] = kort.labels_

#1 numara
# Kazancına göre ortalama alışveriş yapanlar
print(veri[veri["kümeler"]==0].head(5))
#2 numara
# Kazancına göre alışveriş çok az alışveriş yapanlar
print(veri[veri["kümeler"]==1].head(5))
#3 numara Kazancına göre ortalamanın altında alışveriş yapanlar
print(veri[veri["kümeler"]==2].head(5))
#4 numara Kazancına göre alışverişi çok yapanlar
print(veri[veri["kümeler"]==3].head(5))
pd.set_option('display.max_columns', None)