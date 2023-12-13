from PIL import Image
from sklearn import neighbors
import matplotlib.pyplot as plt
import numpy as np
import easygui
import os
import math
import csv

#remplace les nuances de gris par du blanc pour simplifier la comparaison
def grey_to_white(img):
    for l in range(len(img)):
        for c in range(len(img[0])):
            if img[l,c][0] > 100 :
                img[l,c] = [255,255,255]
    return img
#on prépare les images de référence pour chaque chiffre
ref = []
for x in range(10):
    img = np.array(Image.open('./Images de référence/' + str(x) + '.png'))
    ref.append([img,x])


#isole la portion d'une image à partir des coordonnées d'une liste [l1, c1, l2, c2]
#adapte également ces coordonnées selon l'echelle entre la taille de l'image observée et de celle qui a servi à déterminer ces coordonnées
def segmentation(image, coord):
    coeff = image.shape[0] / 2436
    p1 = round(coord[0] * coeff)
    p2 = round(coord[1] * coeff)
    p3 = round(coord[2] * coeff)
    p4 = round(coord[3] * coeff)
    seg = image[p1:p3, p2:p4]
    return seg


#redimensionne une image en fonction d'une autre, testée uniquement pour diminuer
def ajuster_image(img_a_ajuster, img_ref):
    coeff = img_a_ajuster.shape[0] / img_ref.shape[0]

    #créé une copie de img_ref, indépendante de cette dernière (modifier img_finale ne modifie pas img_ref et vice versa)
    img_finale = np.copy(img_ref)

    compteur_colonne = 0 #compte les colonnes pour la boucle en cours
    compteur_ligne = 0 #compte les lignes pour la boucle en cours
    colonne_cible = 0 #total de pixels sur la colonne en cours
    ligne_cible = 0 #total de pixels sur la ligne en cours

    coeff_up = math.ceil(coeff)
    coeff_down = math.floor(coeff)

    for x in img_finale:
        for y in x:
            for z in range(3):
                y[z] = img_a_ajuster[ligne_cible, colonne_cible][z]
            if coeff*compteur_colonne <= colonne_cible:
                colonne_cible = colonne_cible + coeff_down
            else:
                colonne_cible = colonne_cible + coeff_up
            compteur_colonne+=1
        colonne_cible = 0
        compteur_colonne = 0
        if coeff*compteur_ligne <= ligne_cible:
            ligne_cible = ligne_cible + coeff_down
        else:
            ligne_cible = ligne_cible + coeff_up
        compteur_ligne+=1
    return img_finale


#compare l'image d'un chiffre avec les image de référence pour l'identifier
#la variable "a" est le nombre d'erreur rencontrées
def reconnaissance_chiffre(image):
    ranking = []
    for img_ref in ref:
        a=0
        for x, y in zip(ajuster_image(img_ref[0], image), image):
            for x2, y2 in zip(x, y):
                if x2[0] != y2[0]:
                    a+=1
        ranking.append(a)

    correspondance = ranking.index(min(ranking))
    return correspondance

#emplacement des chiffres à récupérer
#tous les chiffres suivants sont de dimension 192*134
locations = [
    [599, 51, 791, 185],
    [599, 207, 791, 341],
    [599, 417, 791, 551],
    [599, 573, 791, 707]
]

Temps = []

#on boucle sur le dossier contenant les images
for image in os.listdir("./sport"):

    #ouverture de l'image à tester
    myimg = Image.open("./sport/" + image)
    img = np.array(myimg)

    chrono_total = []

    #extraction du chiffre et identification
    for coord in locations:
        sample = segmentation(img, coord)
        reponse = reconnaissance_chiffre(sample)
        chrono_total.append(str(reponse))

    Temps.append(chrono_total)
    print('Le temps total est de ' + chrono_total[0] + chrono_total[1] + ' minutes et ' + chrono_total[2] + chrono_total[3] + ' secondes')

with open("sport.csv", "a") as file:
    for x in Temps:
        file.write(x[0] + x[1] + ':' + x[2] + x[3] + "\n")
