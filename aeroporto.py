# -*- coding: utf-8 -*-
"""AEROPORTO.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1V-65jdZrGhbc7yyw7XBqk-2O8fmX8t4j
"""

from google.colab import files
import io
import pandas as pd
import math
import matplotlib.pyplot as plt
upload=files.upload()
dataset =pd.read_csv(io.BytesIO(upload['airports.csv']))

# aeroportos de Bahia
bahia=dataset.query('iso_region=="BR-BA" & longitude_deg>-48.  & type!="closed"')
#bahia.info()

xbahia=bahia['longitude_deg']
ybahia=bahia['latitude_deg']
plt.figure(figsize=(10,10))
plt.scatter(xbahia,ybahia)
naero=len(xbahia)
print(naero)
plt.grid(True)



for Eport in bahia.to_dict("records"):
    lstAero=bahia.to_dict("records")
    lstAero.sort(key = lambda R: (math.sqrt((Eport['longitude_deg'] - R['longitude_deg'])**2 + (Eport['latitude_deg'] - R['latitude_deg'])**2)))
    plt.plot([Eport['longitude_deg'],lstAero[1]["longitude_deg"]], [Eport['latitude_deg'],lstAero[1]["latitude_deg"]])
    plt.plot([Eport['longitude_deg'],lstAero[2]["longitude_deg"]], [Eport['latitude_deg'],lstAero[2]["latitude_deg"]])
    plt.plot([Eport['longitude_deg'],lstAero[3]["longitude_deg"]], [Eport['latitude_deg'],lstAero[3]["latitude_deg"]])

        
            

plt.show()