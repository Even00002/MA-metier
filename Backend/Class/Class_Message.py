"""
Nom du fichier : Class_Message.py
Auteur : David Vilela
Date de création : 26.01.2026
Date de modification : 28.01.2026
"""

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from Backend.DB.db_schema import Base

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    Content = Column(String(45), nullable=False)
    sending_date = Column(Date, nullable=False)

    domains_id = Column(Integer, ForeignKey("domains.id"))

    def __repr__(self):
        return f"id: {self.id}, content: {self.Content}, date: {self.sending_date}, domain: {self.domains_id}"
