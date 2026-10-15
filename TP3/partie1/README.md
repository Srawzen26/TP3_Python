# Dog Guesser

J'ai fait un jeu web où il faut deviner la race d'un chien à partir d'une photo, en Python avec NiceGUI pour ne pas avoir à écrire de JS à côté.

## Comment ça joue

On tape un pseudo, on clique sur Jouer : j'ai prévu 10 manches, avec une photo et 4 races proposées à chaque fois. Plus on répond vite, plus on gagne de points (100 de base, -5 par seconde, minimum 10 si bonne réponse). J'enregistre le score, le record du joueur et le record absolu à la fin, avec un bouton pour voir l'histogramme des parties passées.

## Fichiers

- **app.py** — l'interface NiceGUI et la logique de jeu, c'est lui que j'ai mis comme point d'entrée.
- **dogs.py** — j'y ai mis tous les appels à l'API publique [dog.ceo](https://dog.ceo/dog-api/) (races, photo random, choix, nom lisible).
- **scores.py** — la lecture/écriture des scores dans `data/scores.csv`.

Je n'ai fait charger les races qu'une seule fois, partagées entre tous les joueurs, et j'ai fait en sorte que le record absolu se mette à jour en direct chez tout le monde sans recharger la page.

## Lancer

```bash
pip install -r requirements.txt
python app.py
```

`http://localhost:8081`



- `data/scores.csv` se crée tout seul au premier score.
- `scores.json` à la racine, c'est un reste d'un ancien test que j'ai laissé traîner, il ne sert à rien, je peux le supprimer.
- Je n'ai pas géré les doublons de pseudo (même pseudo = même record).
