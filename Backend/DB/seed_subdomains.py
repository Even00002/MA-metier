"""
Nom du fichier : seed_subdomains.py
Auteur : Joel Cunha Faria
Date de création : 22.01.2026
Date de modification : 22.01.2026
"""

from sqlalchemy import select
from sqlalchemy.orm import Session
from db_schema import engine
from Backend.Class.Class_SubDomain import SubDomain
from Backend.Class.Class_Domain import Domain

def add_subdomain(domain_name: str, sub_name: str, information: str):
    with Session(engine) as session:

        # Récupérer le Domain
        domain = session.execute(
            select(Domain).where(Domain.name == domain_name)
        ).scalar_one_or_none()

        if not domain:
            print(f"Domain introuvable : {domain_name}")
            return

        # Vérifier si le SubDomain existe déjà pour ce Domain
        exists = session.execute(
            select(SubDomain)
            .where(
                SubDomain.name == sub_name,
                SubDomain.domain == domain
            )
        ).scalar_one_or_none()

        if exists:
            print(f"Déjà présent : {sub_name} ({domain_name})")
            return

        # Création ORM (relation directe)
        subdomain = SubDomain(
            name=sub_name,
            information=information,
            domain=domain
        )

        session.add(subdomain)
        session.commit()

        print(f"Ajouté : {sub_name} → {domain_name}")

if __name__ == "__main__":
    add_subdomain("Programmation", "Python", "")
    add_subdomain("Programmation", "C#", "")
    add_subdomain("Programmation", "JavaScript", "")
    add_subdomain("Programmation", "C++", "")
    add_subdomain("Programmation", "Java", "")