"""
Nom du fichier : auth_service.py
Auteur : Joel Cunha Faria
Date de création : 23.01.2026
Date de modification : 23.01.2026
"""
from sqlalchemy.orm import Session
from Backend.DB.db_schema import engine
from Backend.Class.Class_User import User
from sqlalchemy import select
from datetime import datetime
import Backend.session as session

class AuthService:

    @staticmethod
    def login(login: str, password: str):
        with Session(engine) as session:
            stmt = select(User).where(
                (User.email == login) | (User.username == login)
            )

            user = session.execute(stmt).scalar_one_or_none()

            if user is None:
                return False, "Utilisateur introuvable"

            print("USER TROUVÉ :", user)

            if user.password != password:
                return False, "Mot de passe incorrect"

            return True, user

    @staticmethod
    def signup(username: str, email: str, birthdate: str, password: str):
        with Session(engine) as session:

            # Vérifier username ou email déjà existant
            stmt = select(User).where(
                (User.username == username) | (User.email == email)
            )
            if session.execute(stmt).scalar_one_or_none():
                return False, "Utilisateur ou email déjà utilisé"

            try:
                birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
            except ValueError:
                return False, "Format de date invalide (YYYY-MM-DD)"

            user = User(
                username=username,
                email=email,
                birthdate=birthdate,
                password=password,
                role="membre"
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            return True, user

    @staticmethod
    def is_admin():
        if session.current_user is None:
            return False, "Aucun utilisateur connecté"

        if session.current_user.role != "admin":
            return False, "Vous n'êtes pas administrateur"

        return True, session.current_user
