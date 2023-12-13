#on importe les package nécéssaires
import requests
from bs4 import BeautifulSoup
import csv

#on récupère le code source du site dont on souhaite les informations
url = "https://www.gov.uk/search/news-and-communications"
page = requests.get(url)


#on on créé un objet beautiful soup avec les données
soup = BeautifulSoup(page.content, features="html.parser")

#on créé une fonction qui renvoi un tableau avec les données de la balise
#et de la classe ciblée
def bs_to_list(balise_cible, classe_cible):
    resultat = []
    data_bs = soup.find_all(balise_cible, class_=classe_cible)
    for results_bs in data_bs:
        resultat.append(results_bs.string)
    return resultat

#on remplit des listes avec les données ciblées
titre = bs_to_list("a", "gem-c-document-list__item-title")
description = bs_to_list("p", "gem-c-document-list__item-description")

#on ouvre un nouveau fichier csv et on le remplit avec les listes préparées
with open("data.csv","w") as fichier_csv:

    writer = csv.writer(fichier_csv, delimiter=";")
    writer.writerow(["Titre", "Description"])

    for titre, description in zip(titre, description):
        writer.writerow([titre, description])
