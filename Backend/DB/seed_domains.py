"""
Nom du fichier : seed_domains.py
Auteur : Joel Cunha Faria
Date de création : 21.01.2026
Date de modification : 22.01.2026
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from db_schema import engine
from Backend.Class.Class_Domain import Domain
from Backend.Class.Class_SubDomain import SubDomain

def add_domain(name: str):
    with Session(engine) as session:

        exists = session.execute(
            select(Domain).where(Domain.name == name)
        ).scalar_one_or_none()

        if exists:
            print(f"Déjà présent : {name}")
            return

        domain = Domain(name=name)
        session.add(domain)
        session.commit()

        print(f"Ajouté : {name}")


if __name__ == "__main__":
    add_domain("Programmation")
    add_domain("Web")
    add_domain("Base de données")
    add_domain("Systèmes & Réseaux")
    add_domain("Outils & Méthodes")
    add_domain("Aide scolaire IT")