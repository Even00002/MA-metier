"""
Nom du fichier : Class_User.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 28.01.2026
"""
from sqlalchemy import Column, Integer, String, Date, Boolean
from Backend.DB.db_schema import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    email = Column(String(175), nullable=False)
    birthdate = Column(Date, nullable=False)
    role = Column(String(10), nullable=False)
    is_banned = Column(Boolean, nullable=False)
    is_muted = Column(Boolean, nullable=False)

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, username: {self.username}, password: {self.password}, email: {self.email}, birthdate: {self.birthdate}, role: {self.role}")


