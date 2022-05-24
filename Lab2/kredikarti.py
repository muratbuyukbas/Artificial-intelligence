#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  8 12:05:10 2021

@author: muratbuyukbas
"""

#Kredi kartı SOM ile kümeleme

import pandas as pd
import SimpSOM as sps
from sklearn.cluster import KMeans
import numpy as np


#Verilerin hazırlanması
veri = pd.read_csv("kredi_karti.csv")


#Null değerleri yama yapma
pd.isnull(veri).sum()
#kredi limitindeki null değeri yama yapma
missing_index = veri[veri["CREDIT_LIMIT"].isnull()].index.to_list()
veri = veri.drop(index=missing_index[0])
#minumum ödeme null değerleri yama yapma
veri["MINIMUM_PAYMENTS"] = veri["MINIMUM_PAYMENTS"].fillna(veri["MINIMUM_PAYMENTS"].median())


X = veri.drop(["CUST_ID", "TENURE"], axis=1)

#Ağ oluşturma
net = sps.somNet(20,20, X.values)

#Eğitim
net.train(0.01, 10000)

#Veri noktalarının 2 boyutlu haritaya gömülmesi ve kümeleme yapılması
hrt = np.array((net.project(X.values)))
kort = KMeans(n_clusters=3)

#Örneklerin hangi kümeye ait olduğunun belirlenmesi
y_ort = kort.fit_predict(hrt)

#Kümeleri etikeleme
veri["kümeler"] = kort.labels_

#1 numaralı küme büyük
print(veri[veri["kümeler"]==0].head(5))
#2 numaralı küme düşük
print(veri[veri["kümeler"]==1].head(5))
#3 numaraları küme orta
print(veri[veri["kümeler"]==2].head(5))
pd.set_option('display.max_columns', None)
              