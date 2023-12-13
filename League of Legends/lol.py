import requests
from bs4 import BeautifulSoup
import csv
import time
import enlighten

#on définit la liste des champions à importer
liste_des_champions_en = []
with open("champions.txt") as file:
    for x in file:
        liste_des_champions_en.append(x[:-1])

#on récupère les nom en français pour le résultat find_all
liste_des_champions_fr = []
with open("champions_fr.txt") as file:
    for x in file:
        liste_des_champions_fr.append(x[:-1])

all_stats = [] #la liste qui accuiellera toutes les stats récupérées sur la page web

#pour chaque champion on récupère ses stats
#avec une barre de chargement pbar
pbar = enlighten.Counter(total = len(liste_des_champions_en))

for champion_txt_en, champion_txt_fr in zip(liste_des_champions_en, liste_des_champions_fr):

    current_champion_stat = []
    current_champion_stat.append(champion_txt_fr)

    #on importe les données pour le champion en cours, en adaptant certains caractères si besoin
    url = "https://leagueoflegends.fandom.com/wiki/" + champion_txt_en.replace(" ", "_").replace("'", "%27") + "/LoL"
    page = requests.get(url)

    #on les stocke dans un objet BeautifulSoup
    soup = BeautifulSoup(page.content.lower(), features="html.parser")

    #on prépare les id à cibler dans la page html
    #les changements de caractères sont différente que pour l'url
    #certains champions sont nommés différement
    champion = champion_txt_en.replace(" ", "").replace("'", "").replace(".", "").lower()

    if champion == "wukong":
        champion = "monkeyking"

    if champion == "kled":
         champion = "kled1"

    if champion == "renataglasc":
        champion = "renata"

    id_tag_html = [
        "health_" + champion,
        "health_" + champion + "_lvl",
        "resourcebar_" + champion,
        "resourcebar_" + champion + "_lvl",
        "attackdamage_" + champion,
        "attackdamage_" + champion + "_lvl",
        "armor_" + champion,
        "armor_" + champion + "_lvl",
        "magicresist_" + champion,
        "magicresist_" + champion + "_lvl",
        "movementspeed_" + champion,
        "attackspeedbonus_" + champion + "_lvl",
        "attackrange_" + champion
        ]

    #on récupère les stats recherchées dans la page importée
    for page_data in id_tag_html:
        if len(soup.find_all(id=page_data)) > 0:
            #on transforme le string en float puis inversement pour retirer l'éventuelle signe "+"
            #on change le "." en "," pour correspondre au séparateur Excel
            current_champion_stat.append(str(float(soup.find_all(id=page_data)[0].string)).replace(".", ","))
        else:
            current_champion_stat.append("N/A")

    #on ajoute l'attaque speed qui doit être recherchée différement
    if len(soup.find_all("div", class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color")) > 0:
        current_champion_stat.append(soup.find_all("div", class_="pi-smart-data-value pi-data-value pi-font pi-item-spacing pi-border-color")[10].get_text()[7:12].replace(".", ","))
    else:
        current_champion_stat.append("N/A")

    #on ajoute les stats du champion à la liste qui contient toutes les stats de tous les champions
    all_stats.append(current_champion_stat)

    pbar.update()

#On prépare le fichier final qui recevra les données
titre_colonne = [
    "Champion",
    "PDV",
    "PDV par niveau",
    "Mana/Énergie",
    "Mana/Énergie par niveau",
    "Attaque",
    "Attaque par niveau",
    "Armure",
    "Armure par niveau",
    "Resistance magique",
    "Res magique par niveau",
    "Vitesse de déplacement",
    "Vitesse d'attaque par niveau",
    "Portée d'attaque",
    "Vitesse d'attaque"
    ]

with open("lol.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter = ";")
    writer.writerow(titre_colonne)
    for ligne in all_stats:
        writer.writerow(ligne)
