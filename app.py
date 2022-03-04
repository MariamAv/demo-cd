"""
    Projet de démo pour la création d'un CD
"""
from flask import Flask
import os

# Récupération des ENVs
HOST = os.getenv("HOST", "0.0.0.0")
PORT = os.getenv("PORT", "80")
app = Flask("demo")

@app.get("/")
def hello():
    """Foncton appelée pour le chemin par défaut

    Returns:
        str: un message de la plus grande importance
    """
    return "Hello World !"

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
    
    
    
