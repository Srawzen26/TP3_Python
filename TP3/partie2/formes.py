# Champs attendus pour chaque forme (en plus de "shape" et "color")
CHAMPS = {
    "point": ["x", "y"],
    "line": ["x1", "y1", "x2", "y2"],
    "circle": ["x", "y", "radius"],
    "rectangle": ["x", "y", "width", "height"],
    "square": ["x", "y", "cote"],
}


def est_valide(forme: dict) -> bool:
    champs = CHAMPS.get(forme.get("shape"))
    if champs is None:
        return False
    return all(c in forme for c in champs + ["color"])

