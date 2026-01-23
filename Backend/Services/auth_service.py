"""
Nom du fichier : seed_domains.py
Auteur : Joel Cunha Faria
Date de création : 23.01.2026
Date de modification : 23.01.2026
"""
from sqlalchemy import select
from Backend.DB.db_schema import engine
from Backend.Class.Class_User import User

class AuthService:

    @staticmethod
    def login(login: str, password: str):
        with engine.begin() as conn:
            stmt = select(User).where(
                (User.email == login) | (User.username == login)
            )

            user = conn.execute(stmt).scalar_one_or_none()

            if user is None:
                return False, "Utilisateur introuvable"

            if user.password != password:
                return False, "Mot de passe incorrect"

            return True, user