import requests

from formes import CHAMPS

URL = "http://localhost:8000/draw"


def demander_forme() -> dict | None:
    """Pose les questions à l'utilisateur, renvoie la forme ou None pour quitter"""
    nom = input(f"Forme {list(CHAMPS)} (vide pour quitter) : ").strip()
    if nom == "":
        return None
    if nom not in CHAMPS:
        print("Forme inconnue")
        return {}

    forme = {"shape": nom}
    for champ in CHAMPS[nom]:
        forme[champ] = float(input(f"  {champ} : "))
    couleur = input("  couleur r,g,b (ex : 120,200,102) : ")
    forme["color"] = [int(v) for v in couleur.split(",")]
    return forme


while True:
    try:
        forme = demander_forme()
    except ValueError:
        print("Valeur invalide, on recommence")
        continue

    if forme is None:
        break
    if forme == {}:
        continue

    try:
        reponse = requests.post(URL, json=forme, timeout=5)
        print("Envoyé" if reponse.ok else f"Refusé ({reponse.status_code})")
    except requests.RequestException:
        print("Serveur injoignable, est-ce qu'il est lancé ?")