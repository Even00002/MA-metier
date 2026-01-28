"""
Nom du fichier : Class_User_Send_Message.py
Auteur : David Vilela
Date de création : 26.01.2026
Date de modification : 28.01.2026
"""

from sqlalchemy import Column, Integer, ForeignKey
from Backend.DB.db_schema import Base

class UserSendMessage(Base):
    __tablename__ = "users_send_messages"

    id = Column(Integer, primary_key=True)

    users_id = Column(Integer, ForeignKey("users.id"))
    messages_id = Column(Integer, ForeignKey("messages.id"))

    def __repr__(self):
        return f"user_id: {self.users_id}, message_id: {self.messages_id}"
