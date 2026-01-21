"""
Nom du fichier : Class_Domain.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 19.01.2026
"""
from sqlalchemy import Column, Integer, String, Date
from Backend.DB.db_schema import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    information = Column(String(500), nullable=False)

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, name: {self.name}, information: {self.information}")
