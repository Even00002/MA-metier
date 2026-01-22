"""
Nom du fichier : init_db.py
Auteur : Joel Cunha Faria
Date de création : 19.01.2026
Date de modification : 22.01.2026
"""
from Backend.DB.db_schema import engine, Base

# IMPORT OBLIGATOIRE DES CLASSES
from Backend.Class.Class_User import User
from Backend.Class.Class_Domain import Domain
from Backend.Class.Class_SubDomain import SubDomain

def init_db():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    init_db()
