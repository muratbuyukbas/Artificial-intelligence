#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:46:05 2021

@author: muratbuyukbas
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder

veri = pd.read_csv("diyabet.csv")

#sınıf sayısı
label_encoder = LabelEncoder().fit(veri.output)
labels = label_encoder.transform(veri.output)
classes = list(label_encoder.classes_)

#girdi ve çıktılar
X = veri.drop(["output"], axis=1)
y = labels

#veri standartlaştırma
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X = sc.fit_transform(X)

#eğitim ve test verilerini ayırma
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

#çıktı değerleri kategorize
from tensorflow.keras.utils import to_categorical

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

#Model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
model = Sequential()
model.add(Dense(8, input_dim=8, activation="relu"))
model.add(Dense(6, activation="relu"))
model.add(Dense(2, activation="sigmoid"))
model.summary()

#Derleme
model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])

#Eğitim
model.fit(X_train, y_train, validation_data = (X_test, y_test), epochs=40)

#Başarı değerleri
print("Ortalama eğitim kaybı: ", np.mean(model.history.history["loss"]))
print("Ortalama eğitim başarısı: ", np.mean(model.history.history["accuracy"]))
print("Ortalama doğrulama kaybı: ", np.mean(model.history.history["val_loss"]))
print("Ortalama doğrulama başarımı: ", np.mean(model.history.history["val_accuracy"]))



import sklearn.metrics as metrics

#ROC eğrisi için fpr ve tpr hesaplama
probs = model.predict_proba(X_test)
preds = probs[:,1]
fpr, tpr, threshold = metrics.roc_curve(y_test, preds)
roc_auc = metrics.auc(fpr, tpr)



#Eğitim ve değerlendirme sonuçlarını grafikleştirme
import matplotlib.pyplot as plt

plt.plot(model.history.history["accuracy"])
plt.plot(model.history.history["val_accuracy"])
plt.title("Model Başarımları")
plt.ylabel("Başarım")
plt.xlabel("Epok sayısı")
plt.legend(["Eğitim", "Test"], loc="upper left")
plt.show()


plt.plot(model.history.history["loss"])
plt.plot(model.history.history["val_loss"])
plt.title("Model Kayıpları")
plt.ylabel("Kayıp")
plt.xlabel("Epok sayısı")
plt.legend(["Eğitim", "Test"], loc="upper left")
plt.show()

#ROC EĞRİSİ
plt.title("ROC Eğrisi")
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = "lower right")
plt.plot([0,1],[0,1], 'r--')
plt.xlim([0,1])
plt.ylim([0,1])
plt.ylabel("Doğru-pozitif oran")
plt.xlabel("Yanlış-pozitif oran")
plt.show()