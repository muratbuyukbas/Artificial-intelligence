#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 17:34:45 2021

@author: muratbuyukbas
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

#Girdiler
bulasikMiktari = ctrl.Antecedent(np.arange(0,101,1), "bulaşık miktarı")
kirlilikDerecesi = ctrl.Antecedent(np.arange(0,100.1,0.1), "kirlilik oranı")
bulasikCinsi = ctrl.Antecedent(np.arange(0,100.1,0.1), "bulaşık cinsi")

#Çıktılar
yikamaZamani = ctrl.Consequent(np.arange(30,161,1), "yıkama zamanı")
deterjanMiktari = ctrl.Consequent(np.arange(0,100.1,0.1), "deterjan miktarı")
suSicakligi = ctrl.Consequent(np.arange(35,67.6,0.1), "su sıcaklığı")
ustPompaDevir = ctrl.Consequent(np.arange(2100,3600,100), "üst pompa devri")
altPompaDevir = ctrl.Consequent(np.arange(2100,3600,100), "alt pompa devri")

#Girdi değerleri için üyelik fonsiyonlarını belirlemek
bulasikMiktari.automf(3)
kirlilikDerecesi.automf(3)
bulasikCinsi.automf(3)

#Çıktı değerleri için üyelik fonsiyonlarını belirlemek
yikamaZamani.automf(5)
deterjanMiktari.automf(5)
suSicakligi.automf(3)
ustPompaDevir.automf(5)
altPompaDevir.automf(5)


#Bulanık mantık kurallarını belirlemek

kural1 = ctrl.Rule(bulasikMiktari["poor"] & kirlilikDerecesi["poor"] & bulasikCinsi["poor"],
                   (yikamaZamani["poor"], deterjanMiktari["poor"], suSicakligi["poor"],
                   ustPompaDevir["poor"], altPompaDevir["poor"]))
kural2 = ctrl.Rule(bulasikMiktari["poor"] & kirlilikDerecesi["good"] & bulasikCinsi["average"],
                   (yikamaZamani["average"], deterjanMiktari["average"], suSicakligi["good"],
                   ustPompaDevir["mediocre"], altPompaDevir["good"]))
kural3 = ctrl.Rule(bulasikMiktari["average"] & kirlilikDerecesi["average"] & bulasikCinsi["good"],
                   (yikamaZamani["average"], deterjanMiktari["average"], suSicakligi["average"],
                   ustPompaDevir["good"], altPompaDevir["good"]))
kural4 = ctrl.Rule(bulasikMiktari["good"] & kirlilikDerecesi["good"] & bulasikCinsi["average"],
                   (yikamaZamani["good"], deterjanMiktari["good"], suSicakligi["good"],
                   ustPompaDevir["mediocre"], altPompaDevir["good"]))

#Çıktıların belirlenmesi
ciktiKontrol = ctrl.ControlSystem([kural1, kural2, kural3, kural4])
ciktiBelirleme = ctrl.ControlSystemSimulation(ciktiKontrol)

# Kural 1 için Çıktıların Hesaplanması
ciktiBelirleme.input["bulaşık miktarı"] = 18
ciktiBelirleme.input["kirlilik oranı"] = 15.1
ciktiBelirleme.input["bulaşık cinsi"] = 12.7
ciktiBelirleme.compute()
print("Yıkama Zamanı: ", ciktiBelirleme.output["yıkama zamanı"],
      "\nDeterjan Miktarı: ", ciktiBelirleme.output["deterjan miktarı"],
      "\nSu Sıcaklığı: ", ciktiBelirleme.output["su sıcaklığı"],
      "\nÜst Pompa Devri: ", ciktiBelirleme.output["üst pompa devri"],
      "\nAlt Pompa Devri: ", ciktiBelirleme.output["alt pompa devri"])


yikamaZamani.view(sim=ciktiBelirleme)
deterjanMiktari.view(sim=ciktiBelirleme)
suSicakligi.view(sim=ciktiBelirleme)
ustPompaDevir.view(sim=ciktiBelirleme)
altPompaDevir.view(sim=ciktiBelirleme)


# Kural 2 için Çıktıların Hesaplanması
ciktiBelirleme.input["bulaşık miktarı"] = 22
ciktiBelirleme.input["kirlilik oranı"] = 70.4
ciktiBelirleme.input["bulaşık cinsi"] = 50
ciktiBelirleme.compute()
print("Yıkama Zamanı: ", ciktiBelirleme.output["yıkama zamanı"],
      "\nDeterjan Miktarı: ", ciktiBelirleme.output["deterjan miktarı"],
      "\nSu Sıcaklığı: ", ciktiBelirleme.output["su sıcaklığı"],
      "\nÜst Pompa Devri: ", ciktiBelirleme.output["üst pompa devri"],
      "\nAlt Pompa Devri: ", ciktiBelirleme.output["alt pompa devri"])

"""
yikamaZamani.view(sim=ciktiBelirleme)
deterjanMiktari.view(sim=ciktiBelirleme)
suSicakligi.view(sim=ciktiBelirleme)
ustPompaDevir.view(sim=ciktiBelirleme)
altPompaDevir.view(sim=ciktiBelirleme)
"""

# Kural 3 için Çıktıların Hesaplanması
ciktiBelirleme.input["bulaşık miktarı"] = 62
ciktiBelirleme.input["kirlilik oranı"] = 40.1
ciktiBelirleme.input["bulaşık cinsi"] = 88.7
ciktiBelirleme.compute()
print("Yıkama Zamanı: ", ciktiBelirleme.output["yıkama zamanı"],
      "\nDeterjan Miktarı: ", ciktiBelirleme.output["deterjan miktarı"],
      "\nSu Sıcaklığı: ", ciktiBelirleme.output["su sıcaklığı"],
      "\nÜst Pompa Devri: ", ciktiBelirleme.output["üst pompa devri"],
      "\nAlt Pompa Devri: ", ciktiBelirleme.output["alt pompa devri"])

"""
yikamaZamani.view(sim=ciktiBelirleme)
deterjanMiktari.view(sim=ciktiBelirleme)
suSicakligi.view(sim=ciktiBelirleme)
ustPompaDevir.view(sim=ciktiBelirleme)
altPompaDevir.view(sim=ciktiBelirleme)
"""

# Kural 4 için Çıktıların Hesaplanması
ciktiBelirleme.input["bulaşık miktarı"] = 90
ciktiBelirleme.input["kirlilik oranı"] = 98
ciktiBelirleme.input["bulaşık cinsi"] = 62
ciktiBelirleme.compute()
print("Yıkama Zamanı: ", ciktiBelirleme.output["yıkama zamanı"],
      "\nDeterjan Miktarı: ", ciktiBelirleme.output["deterjan miktarı"],
      "\nSu Sıcaklığı: ", ciktiBelirleme.output["su sıcaklığı"],
      "\nÜst Pompa Devri: ", ciktiBelirleme.output["üst pompa devri"],
      "\nAlt Pompa Devri: ", ciktiBelirleme.output["alt pompa devri"])

"""
yikamaZamani.view(sim=ciktiBelirleme)
deterjanMiktari.view(sim=ciktiBelirleme)
suSicakligi.view(sim=ciktiBelirleme)
ustPompaDevir.view(sim=ciktiBelirleme)
altPompaDevir.view(sim=ciktiBelirleme)
"""
