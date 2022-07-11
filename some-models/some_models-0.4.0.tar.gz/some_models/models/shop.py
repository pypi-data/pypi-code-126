from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from some_models.models.base import Base


class Shop(Base):
    __tablename__ = "shop"

    name = Column(String, nullable=False, unique=True)

    products = relationship("Product", back_populates="shop")
