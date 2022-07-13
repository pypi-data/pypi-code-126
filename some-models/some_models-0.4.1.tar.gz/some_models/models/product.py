from sqlalchemy import Column, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from some_models.models.base import Base


class Product(Base):
    __tablename__ = "product"

    name = Column(String, nullable=False, unique=True)
    price_usd = Column(Float, nullable=False)
    shop_id = Column(
        ForeignKey("shop.id", ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False,
    )

    shop = relationship("Shop", back_populates="products")
    purchases = relationship("Purchase", back_populates="product")
