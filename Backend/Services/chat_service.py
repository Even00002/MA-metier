"""
Nom du fichier : chat_service.py
Auteur : David Vilela
Date de création : 26.01.2026
Date de modification : 29.01.2026
"""

from datetime import date
from sqlalchemy import select
from Backend.DB.db_schema import Session  # factory de session

from Backend.Class.Class_User import User
from Backend.Class.Class_Domain import Domain
from Backend.Class.Class_Message import Message
from Backend.Class.Class_User_Send_Message import UserSendMessage


class ChatService:

    @staticmethod
    def send_message(user_id: int, domain_id: int, content: str):
        """
        Envoie un message dans un domaine
        """
        with Session() as session:
            # Vérifie que l'utilisateur existe
            user = session.execute(
                select(User).where(User.id == user_id)
            ).scalar_one_or_none()

            if user is None:
                return False, "Utilisateur introuvable"

            # Vérifie que le domaine existe
            domain = session.execute(
                select(Domain).where(Domain.id == domain_id)
            ).scalar_one_or_none()

            if domain is None:
                return False, "Domaine introuvable"

            # Création du message
            message = Message(
                Content=content,
                sending_date=date.today(),
                domains_id=domain_id
            )
            session.add(message)
            session.flush()  # récupère message.id pour le lien

            # Création du lien UserSendMessage
            link = UserSendMessage(
                users_id=user_id,
                messages_id=message.id
            )
            session.add(link)

            session.commit()  # commit final pour tout sauvegarder

            return True, message

    @staticmethod
    def get_messages_by_domain(domain_id: int):
        """
        Récupère tous les messages d'un domaine avec leur auteur
        """
        with Session() as session:
            stmt = (
                select(
                    Message.id,
                    Message.Content,
                    Message.sending_date,
                    User.username
                )
                .join(UserSendMessage, UserSendMessage.messages_id == Message.id)
                .join(User, User.id == UserSendMessage.users_id)
                .where(Message.domains_id == domain_id)
                .order_by(Message.sending_date)
            )

            results = session.execute(stmt).all()

            messages = []
            for msg in results:
                messages.append({
                    "id": msg.id,
                    "content": msg.Content,
                    "date": msg.sending_date,
                    "username": msg.username  # vrai nom de l'utilisateur
                })

            return True, messages