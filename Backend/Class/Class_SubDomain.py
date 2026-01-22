"""
Nom du fichier : Class_SubDomain.py
Auteur : Joel Cunha Faria
Date de création : 21.01.2026
Date de modification : 22.01.2026
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from Backend.DB.db_schema import Base

class SubDomain(Base):
    __tablename__ = "subdomains"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    information = Column(String(500), nullable=False)

    # Clé étrangère → Domain
    domain_id = Column(Integer, ForeignKey("domains.id"), nullable=False)

    # Relation ORM
    domain = relationship("Domain", back_populates="subdomains")

    def __repr__(self):
        """
            Return a readable string representation of the Person object,
            showing id, firstname, and lastname
        """
        return (f"id: {self.id}, name: {self.name}, information: {self.information}, domain_id: {self.domain_id}")
