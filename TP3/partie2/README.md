# Tableau blanc collaboratif

J'ai fait un canvas partagé en temps réel : ce qu'on envoie depuis un programme terminal apparaît instantanément chez tout le monde qui a la page ouverte. Serveur FastAPI + WebSocket pour la diffusion.

## Comment ça marche

J'ai fait: la page (`static/index.html`) ne fait qu'afficher. C'est `client.py`, que je lance dans un terminal, qui demande une forme, ses coordonnées et une couleur, et l'envoie au serveur en `POST /draw`. Le serveur valide, garde en mémoire, logue dans `formes.log`, et repousse la forme à tous les navigateurs connectés via `/ws`, qui la dessinent. J'ai fait en sorte qu'un navigateur qui se connecte en retard reçoive tout l'historique d'un coup.

## Fichiers

- **server.py** — le serveur FastAPI, avec les routes `/draw` et `/ws`.
- **client.py** — le client terminal que j'ai fait pour envoyer les formes.
- **formes.py** — j'y ai mis la définition des champs attendus par forme (`CHAMPS`) et la validation.
- **static/index.html** — la page avec le canvas.

## Lancer

```bash
pip install -r requirements.txt

# 1er terminal 
python server.py
```

J'ouvre ensuite `http://localhost:8000` (plusieurs onglets possibles).

```bash
# 2 eme terminal 
python client.py
```

Exemple de saisie :
```
Forme [...] (vide pour quitter) : circle
  x : 400
  y : 300
  radius : 50
  couleur r,g,b (ex : 120,200,102) : 200,50,50
```
