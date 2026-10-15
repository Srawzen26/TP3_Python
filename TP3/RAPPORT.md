# TP3 Network parties 1 et 2


Pour la partie 1, j'ai fait le jeu où il faut deviner la race d'un chien. L'image vient de l'API dog.ceo, il y a 4 propositions et 10 manches par partie. Chaque manche rapporte jusqu'à 100 points, et ca peut mettre moins si je mets du temps à répondre, donc 1000 points au maximum. Les parties sont enregistrées dans un fichier CSV. Après j'ai fait en sorte que l'interface montre mon record et le record de tout les utilisateurs, et il change tout seul si un autre le bat. Et pui j'ai aussi ajouté un bouton qui affiche l'histogramme des scores.

Dans la partie 2 on devait faire un tableau blanc partagé. Donc j'ai mit en place un serveur FastAPI qui reçoit les formes sur `POST /draw` (point, ligne, cercle, rectangle, carré) et les renvoie en direct par WebSocket à toutes les pages ouvertes. Ensuite La page dessine ça sur un canvas et un petit client en ligne de commande me demande la forme, les dimensions et la couleur, puis l'envoie au serveur. Le serveur garde aussi une trace de chaque forme dans `formes.log`.



## Ce que j'ai réutilisé du cours

Du TP1, j'ai repris l'environnement virtuel avec son `requirements.txt`, le découpage en modules, les fonctions avec leurs annotations de types, les compréhensions de listes et la boucle `while` avec `input()` pour le client.

Du TP2, j'ai repris l'ouverture de fichiers avec `with open(..., encoding="utf-8")`, le module `os`, `datetime` pour dater chaque score, et `csv.DictReader` / `DictWriter` pour le fichier de scores. Les fonctions `save_score`, `read_highscore` et `read_highscores` viennent aussi de là, tout comme l'histogramme. Le fichier de log du serveur reprend l'idée des logs.

Du TP3 lui-même : `requests` avec la gestion des erreurs réseau, le WebSocket et l'API HTTP côté serveur.



## Comment je l'ai fait

J'ai lu l'énoncé et décidé de ranger le travail en un dossier par partie, pour m'y retrouver. Ensuite j'ai demandé une seconde version qui utilise vraiment ce qu'on a vu en TP1 et TP2, parce que je voulais que le code montre ce que j'ai appris et pas seulement que ça marche.

J'ai essayer de faire un maximum moi meme pendant ce TP, mais il y a certaines parties avec lequels je me suis aider de l'IA, parceque je ne savais pas quels bibliothèques mettre comme pour le websocket et d'autres, je l'ai aussi utiliser pour une bonne partie du `app.py` dans la partie 1, j'avais du mal le faire moi meme, en revanche c'est moi qui l'ai guidé dans ce qu'il faisait pour que je puisse etre sur sur qu'il fasse ce que je veux et pas qu'il decide lui meme de l'application. Et dans la parie 2 c'est assez similaire mise part pour le fichier html dans lequel il m'as grandement aider parceque je ne savais pas le faire du tout, mais maitenant je pense que ca devrait aller, etant donner que j'ai analyser son code pour pouvoir le reproduire de mon coté.
Sinon pour le reste j'ai principalement regarder des doc sur internet ou des projet similaire pour m'aider a le faire.

Ensuite, j'ai lancé le code . Au début il plantait parce que matplotlib n'était pas installé, je l'ai installé et ca a fonctionner. J'ai joué au jeu pour vérifier que les scores s'enregistraient bien. Quand je ne comprenais pas un morceau, je le prenais et aller le corriger parceque certains affichage n'étais pas bon (la fonction `plot_scores` par exemple). Pour le TP2 j'avais aussi comparé avec une réponse de Gemini, pour voir laquelle était la plus simple.

Ce que j'ai principalement chercher, c'est sur les infos que je n'avais pas vus en cours. Je ne connaissais pas FastAPI ni le WebSocket, et le canvas en JavaScript non plus. Etant donner que c'était imposait aussi une interface web en Python seulement, et sans NiceGUI je ne savais pas comment faire. L'IA m'a donné une base qui tourne, que je peux maintenant lire et modifier.

