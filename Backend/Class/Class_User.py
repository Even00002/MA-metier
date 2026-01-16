"""
Nom du fichier : Class_User.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 16.01.2026
"""
from sqlalchemy import Column, Integer, String, Date
from Backend.DB.db_schema import Base

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False)
    password = Column(String(25), nullable=False)
    email = Column(String(175), nullable=False)
    birthdate = Column(Date, nullable=False)
    age = Column(String, nullable=False)
    role = Column(String, nullable=False)

    def __init__(self, **kwargs):
        """
            Initialize a Person instance
            Accepts any keyword arguments and sets firstname and lastname
            This allows creation for CRUD operations
        """
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")
        self.email = kwargs.get("email")
        self.birthdate = kwargs.get("birthdate")
        self.age = kwargs.get("age")
        self.role = kwargs.get("role")

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, username: {self.username}, password: {self.password}, email: {self.email}, birthdate: {self.birthdate}, age: {self.age}, role: {self.role}")


