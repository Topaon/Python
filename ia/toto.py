import spacy

# Charger le modèle pré-entraîné
nlp = spacy.load("en_core_web_sm")

def detecter_salutation(message):
    # Traiter le message avec le modèle spaCy
    doc = nlp(message)

    # Vérifier si le message contient une salutation
    for token in doc:
        if token.text.lower() in ["bonjour", "salut", "coucou", "hello"]:
            return True

    return False

# Exemple d'utilisation
message_utilisateur = input("Entrez votre message : ")
est_salutation = detecter_salutation(message_utilisateur)

if est_salutation:
    print("Le message est une salutation !")
else:
    print("Le message n'est pas une salutation.")
