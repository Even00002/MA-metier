"""
Nom du fichier : Class_Domain.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 16.01.2026
"""
from sqlalchemy import Column, Integer, String, Date
from Backend.DB.db_schema import Base

class Domain(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    information = Column(String(500), nullable=False)

    def __init__(self, **kwargs):
        """
            Initialize a Person instance
            Accepts any keyword arguments and sets firstname and lastname
            This allows creation for CRUD operations
        """
        self.name = kwargs.get("name")
        self.information = kwargs.get("information")

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, name: {self.name}, password: {self.information}")
