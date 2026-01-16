"""
Nom du fichier : db_schema.py
Auteur : Joel Cunha Faria
Date de création : 15.01.2026
Date de modification : 16.01.2026
"""
# --------------------------------- IMPORTS ---------------------------------
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# --------------------------------- ENGINE CONFIGURATION ---------------------------------
engine = create_engine("sqlite:///Backend/DB/database.db")

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