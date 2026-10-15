import json
import os
from datetime import datetime

import uvicorn
from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse

from formes import est_valide

DOSSIER = os.path.dirname(__file__)
JOURNAL = os.path.join(DOSSIER, "formes.log")  # une ligne par forme reçue

app = FastAPI()
tableaux: list[WebSocket] = []  # pages ouvertes en ce moment
historique: list[dict] = []  # pour redessiner chez ceux qui arrivent en retard


@app.get("/")
def page():
    return FileResponse(os.path.join(DOSSIER, "static", "index.html"))


@app.post("/draw")
async def draw(forme: dict):
    if not est_valide(forme):
        raise HTTPException(status_code=422, detail="forme invalide")

    historique.append(forme)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now():%Y-%m-%d %H:%M:%S} | {json.dumps(forme)}\n")

    for tableau in list(tableaux):
        try:
            await tableau.send_json(forme)
        except Exception:
            tableaux.remove(tableau)  # page fermée
    return {"ok": True}


@app.websocket("/ws")
async def ws(websocket: WebSocket):
    await websocket.accept()
    tableaux.append(websocket)
    for forme in historique:
        await websocket.send_json(forme)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        if websocket in tableaux:
            tableaux.remove(websocket)


if __name__ == "__main__":
    uvicorn.run(app, port=8000)