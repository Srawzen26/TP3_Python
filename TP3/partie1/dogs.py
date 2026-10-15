import random

import requests

API = "https://dog.ceo/api"


def get_breeds() -> list[str]:
    """Liste de toutes les races, ex : ['affenpinscher', ..., 'hound-afghan', ...]"""
    reponse = requests.get(f"{API}/breeds/list/all", timeout=10).json()["message"]
    races = []
    for race, sous_races in reponse.items():
        if sous_races:
            for sous_race in sous_races:
                races.append(f"{race}-{sous_race}")  # même nom que dans l'URL des images
        else:
            races.append(race)
    return races


def random_dog() -> tuple[str, str]:
    """Renvoie (url de l'image, race du chien)"""
    url = requests.get(f"{API}/breeds/image/random", timeout=10).json()["message"]
    # url = https://images.dog.ceo/breeds/<race>/<fichier>.jpg
    return url, url.split("/")[-2]


def get_choices(bonne_race: str, races: list[str]) -> list[str]:
    """La bonne race + 3 mauvaises, dans le désordre"""
    autres = [r for r in races if r != bonne_race]
    choix = random.sample(autres, 3) + [bonne_race]
    random.shuffle(choix)
    return choix


def nom_propre(race: str) -> str:
    """'hound-afghan' -> 'afghan hound'"""
    morceaux = race.split("-")
    morceaux.reverse()
    return " ".join(morceaux)