import requests
from bs4 import BeautifulSoup
import csv

#on importe les données de la page
url = "https://www.leagueoflegends.com/en-gb/champions/"
page = requests.get(url)

#on les stocke dans un objet BeautifulSoup
soup = BeautifulSoup(page.content, features="html.parser")

result = soup.find_all(class_="style__Text-n3ovyt-3 gMLOLF")

with open("champions.txt", "a") as file:
    for x in result:
        file.write(x.string + "\n")
