from sqlalchemy import Column, Integer, String, Float
from database import Base

class CleanProduct(Base):
    __tablename__ = 'products'
    __table_args__ = {'schema': 'clean'}

    product_id = Column(Integer, primary_key=True, index=True)
    manufacturer_id = Column(Integer, index=True, nullable=False)
    department = Column(String(15), nullable=True)
    brand = Column(String(100), nullable=True)
    commodity_desc = Column(String(30), nullable=True)
    sub_commodity_desc = Column(String(30), nullable=True)
    curr_size_of_product = Column(String(20), nullable=True)
    
    size_numeric = Column(Float, nullable=True)
    size_unit = Column(String(10), nullable=True)

    def __repr__(self):
        return f"<CleanProduct(product_id={self.product_id}, brand='{self.brand}')>"