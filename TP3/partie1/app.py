import time

import matplotlib.pyplot as plt
import requests
from nicegui import ui

import dogs
import scores

NB_MANCHES = 10  # 10 images x 100 points max = 1000 points max

# partagé entre tous les joueurs : le label du record se met à jour tout seul
partage = {"record": scores.read_record()}
races = []  # chargées au premier lancement d'une partie


@ui.page("/")
def index():
    # état de la partie en cours (propre à chaque onglet)
    partie = {"manche": 0, "total": 0, "debut": 0.0, "bonne_race": ""}

    ui.label("🐶 Dog Guesser").classes("text-3xl font-bold self-center")
    ui.label().bind_text_from(partage, "record").classes("text-lg self-center")
    pseudo = ui.input("Pseudo", value="joueur").classes("self-center")
    perso = ui.label().classes("self-center")
    info = ui.label().classes("text-lg self-center")
    image = ui.image().classes("w-96 self-center")
    boutons = ui.row().classes("self-center")
    message = ui.label().classes("text-lg self-center")

    def commencer():
        if not races:
            try:
                races.extend(dogs.get_breeds())
            except requests.RequestException:
                ui.notify("Impossible de joindre l'API dog.ceo", type="negative")
                return
        partie["manche"] = 0
        partie["total"] = 0
        pseudo.disable()
        bouton_jouer.set_visibility(False)
        perso.text = f"Ton record : {scores.read_highscore(pseudo.value)} pts"
        manche_suivante()

    def manche_suivante():
        partie["manche"] += 1
        if partie["manche"] > NB_MANCHES:
            terminer()
            return
        try:
            url, bonne_race = dogs.random_dog()
        except requests.RequestException:
            ui.notify("Erreur réseau, partie interrompue", type="negative")
            terminer()
            return
        partie["bonne_race"] = bonne_race
        image.set_source(url)
        info.text = f"Manche {partie['manche']}/{NB_MANCHES} - Score : {partie['total']}"
        message.text = ""
        boutons.clear()
        with boutons:
            for race in dogs.get_choices(bonne_race, races):
                ui.button(dogs.nom_propre(race), on_click=lambda race=race: repondre(race))
        partie["debut"] = time.time()

    def repondre(race: str):
        boutons.clear()
        if race == partie["bonne_race"]:
            # 100 points, moins 5 par seconde, 10 points minimum
            secondes = int(time.time() - partie["debut"])
            points = max(10, 100 - 5 * secondes)
            message.text = f"✅ Bravo ! +{points} pts"
        else:
            points = 0
            message.text = f"❌ C'était : {dogs.nom_propre(partie['bonne_race'])}"
        partie["total"] += points
        ui.timer(1.5, manche_suivante, once=True)

    def terminer():
        boutons.clear()
        pseudo.enable()
        if partie["total"] > 0:
            scores.save_score(pseudo.value, partie["total"])
            partage["record"] = scores.read_record()
        info.text = f"Partie terminée : {partie['total']} / {NB_MANCHES * 100}"
        perso.text = f"Ton record : {scores.read_highscore(pseudo.value)} pts"
        bouton_jouer.text = "Rejouer"
        bouton_jouer.set_visibility(True)

    def histogramme():
        with ui.dialog() as fenetre, ui.card():
            with ui.pyplot(figsize=(6, 4)):
                plt.hist([int(l["score"]) for l in scores.read_all()],
                         bins=range(0, 1100, 100), edgecolor="black")
                plt.xlabel("Score")
                plt.ylabel("Nombre de parties")
            ui.button("Fermer", on_click=fenetre.close)
        fenetre.open()

    bouton_jouer = ui.button("Jouer", on_click=commencer).classes("self-center")
    ui.button("Histogramme des scores", on_click=histogramme).props("flat").classes("self-center")


ui.run(title="Dog Guesser", port=8081, reload=False)

