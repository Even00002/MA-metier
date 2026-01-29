"""
Nom du fichier : subdomain_service.py
Auteur : Joel Cunha Faria
Date de création : 29.01.2026
Date de modification : 29.01.2026
"""
from Backend.DB.db_schema import get_session
from Backend.Class.Class_SubDomain import SubDomain

def get_sujet_text(subdomain_name: str) -> str:
    """
    Récupère le texte explicatif pour un SubDomain depuis la base SQL.
    """
    session = get_session()
    try:
        subdomain = session.query(SubDomain).filter(SubDomain.name == subdomain_name).first()
        if subdomain:
            return subdomain.information
        else:
            return f"Texte non disponible pour le sujet : {subdomain_name}"
    finally:
        session.close()
