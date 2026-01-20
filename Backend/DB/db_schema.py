"""
Nom du fichier : db_schema.py
Auteur : Joel Cunha Faria
Date de création : 15.01.2026
Date de modification : 19.01.2026
"""
# --------------------------------- IMPORTS ---------------------------------
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# --------------------------------- CHEMINS ---------------------------------
# Récupère le chemin absolu du dossier Backend
# __file__ = ce fichier (db_schema.py)
# dirname deux fois permet de remonter à Backend/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Chemin vers le dossier DB (Backend/DB)
DB_DIR = os.path.join(BASE_DIR, "DB")

# Crée le dossier DB s'il n'existe pas encore
# SQLite ne peut pas créer un fichier dans un dossier inexistant
os.makedirs(DB_DIR, exist_ok=True)

# Chemin complet vers le fichier de base de données SQLite
DB_PATH = os.path.join(DB_DIR, "database.db")

# --------------------------------- ENGINE CONFIGURATION ---------------------------------
engine = create_engine(f"sqlite:///{DB_PATH}")

# --------------------------------- DECLARATIVE BASE ---------------------------------
Base = declarative_base()

# --------------------------------- SESSION FACTORY ---------------------------------
SessionLocal = sessionmaker(bind=engine)

# --------------------------------- UTILITY FUNCTION ---------------------------------
def get_session():
    """
    Creates and returns a new SQLAlchemy session
    Used for all CRUD operations
    """
    return SessionLocal()