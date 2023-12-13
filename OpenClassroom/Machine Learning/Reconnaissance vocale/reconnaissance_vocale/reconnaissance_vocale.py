import speech_recognition as sr

def recon():
    r = sr.Recognizer()

    micro = sr.Microphone(device_index=4)

    with micro as source:
        print("Parlez")
        audio_data = r.listen(source)
        print("Fin de l'écoute")

    response = r.recognize_google(audio_data, language="fr-FR")
    return response
