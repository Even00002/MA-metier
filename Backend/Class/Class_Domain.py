"""
Nom du fichier : Class_Domain.py
Auteur : Joel Cunha Faria
Date de création : 16.01.2026
Date de modification : 22.01.2026
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Backend.DB.db_schema import Base

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from Backend.DB.db_schema import Base
from .Class_SubDomain import SubDomain  # <- important pour que SQLAlchemy connaisse SubDomain

class Domain(Base):
    __tablename__ = "domains"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    # 1 Domain → plusieurs SubDomains
    subdomains = relationship(
        "SubDomain",          # nom de la classe liée
        back_populates="domain",  # correspond à la relation dans SubDomain
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        """
        Représentation lisible de l'objet Domain
        """
        return f"Domain(id={self.id}, name='{self.name}')"