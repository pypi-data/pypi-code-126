from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from some_models.models.base import Base


class Purchase(Base):
    __tablename__ = "purchase"

    user_id = Column(
        ForeignKey("user.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    product_id = Column(
        ForeignKey("product.id", ondelete="CASCADE", onupdate="CASCADE")
    )
    quantity = Column(Integer, nullable=False)

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")
