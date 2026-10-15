import csv
import os
from datetime import datetime

DOSSIER = os.path.join(os.path.dirname(__file__), "data")
FICHIER = os.path.join(DOSSIER, "scores.csv")  # colonnes : username, score, date


def save_score(username: str, score: int) -> None:
    os.makedirs(DOSSIER, exist_ok=True)
    nouveau = not os.path.exists(FICHIER)
    with open(FICHIER, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["username", "score", "date"])
        if nouveau:
            writer.writeheader()
        writer.writerow({
            "username": username,
            "score": score,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        })


def read_all() -> list[dict]:
    if not os.path.exists(FICHIER):
        return []
    with open(FICHIER, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def read_highscore(username: str) -> int:
    """Record personnel (0 si le joueur n'a jamais joué)"""
    scores = [int(ligne["score"]) for ligne in read_all() if ligne["username"] == username]
    return max(scores, default=0)


def read_highscores(n: int) -> list[tuple[str, int]]:
    """Les n meilleurs scores de tous les temps"""
    scores = [(ligne["username"], int(ligne["score"])) for ligne in read_all()]
    return sorted(scores, key=lambda x: x[1], reverse=True)[:n]


def read_record() -> str:
    """Texte du record absolu pour l'interface"""
    meilleurs = read_highscores(1)
    if not meilleurs:
        return "Record absolu : aucun pour l'instant"
    nom, score = meilleurs[0]
    return f"Record absolu : {score} pts ({nom})"


