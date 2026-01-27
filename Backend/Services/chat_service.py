"""
Nom du fichier : chat_service.py
Auteur : David Vilela
Date de création : 26.01.2026
"""

from datetime import date
from sqlalchemy import select
from Backend.DB.db_schema import engine

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
        with engine.begin() as conn:

            user = conn.execute(
                select(User).where(User.id == user_id)
            ).scalar_one_or_none()

            if user is None:
                return False, "Utilisateur introuvable"

            domain = conn.execute(
                select(Domain).where(Domain.id == domain_id)
            ).scalar_one_or_none()

            if domain is None:
                return False, "Domaine introuvable"

            message = Message(
                Content=content,
                sending_date=date.today(),
                domains_id=domain_id
            )

            conn.add(message)
            conn.flush()

            link = UserSendMessage(
                users_id=user_id,
                messages_id=message.id
            )

            conn.add(link)

            return True, message

    @staticmethod
    def get_messages_by_domain(domain_id: int):
        """
        Récupère tous les messages d'un domaine avec leur auteur
        """
        with engine.begin() as conn:

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

            results = conn.execute(stmt).all()

            messages = []
            for msg in results:
                messages.append({
                    "id": msg.id,
                    "content": msg.Content,
                    "date": msg.sending_date,
                    "username": msg.username
                })

            return True, messages
