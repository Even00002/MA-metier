"""
Nom du fichier : Class_Domain.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 22.01.2026
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Backend.DB.db_schema import Base

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    # 1 Domain → plusieurs SubDomains
    subdomains = relationship(
        "SubDomain",
        back_populates="domain",
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, name: {self.name}")
