from statistics import variance, covariance
from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

#Récupération des données
house_data = pd.read_csv('house.csv')
house_data = house_data[house_data['loyer'] < 8000]

#Calcul de notre paramètre theta
X = np.array([np.ones(house_data.shape[0]), house_data['surface'].values]).T
y = np.array(house_data['loyer']).T

theta = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

#Création du graphique avec les résultats
#D'abord les données d'entrée
plt.xlabel("Surface")
plt.ylabel("Loyer")
plt.plot(house_data['surface'], house_data['loyer'], 'ro', markersize=4)

#Avec sklearn
reg = linear_model.LinearRegression()
reg.fit(X,y)

#A la main
x = house_data['surface']
y = house_data['loyer']

a = covariance(x,y) / variance(x)
b = y.mean() - a * x.mean()

print(theta)
print(a, b)

#Ensuite le modèle choisi
plt.plot([0,250], [theta.item(0), theta.item(0) + 250 * theta.item(1)], linestyle='--', c='#000000')
plt.plot([0,250], [reg.intercept_, reg.intercept_ + 250 * reg.coef_[1]], linestyle='--', c='#000000')
plt.plot([0,250], [b, b + 250 * a], linestyle='--', c='#000000')

plt.show()
