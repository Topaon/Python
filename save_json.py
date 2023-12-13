import requests
import json

# URL de l'API
url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

# Envoi de la requête GET
response = requests.get(url)

# Vérification de la réponse de la requête
if response.status_code == 200:
    # Récupération des données JSON
    data = response.json()
    print(type(data))

    # Liste pour stocker les noms des cartes
    card_names = []

    # Parcours des éléments dans la réponse JSON
    for card in data['data']:
        card_names.append(card)

    # Affichage de la liste des noms des cartes
    # Serializing json
    json_object = json.dumps(card_names, indent=4)

    # Writing to sample.json
    with open("sample.json", "w") as outfile:
        outfile.write(json_object)
else:
    print("La requête a échoué avec le code d'état :", response.status_code)
