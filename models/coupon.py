from sqlalchemy import Column, Integer, BigInteger, Boolean, PrimaryKeyConstraint
from database import Base

class CleanCoupon(Base):
    __tablename__ = 'coupon'
    __table_args__ = (
        PrimaryKeyConstraint('coupon_upc', 'product_id', 'campaign_id'),
        {'schema': 'clean'}
    )

    coupon_upc = Column(BigInteger, nullable=False)
    product_id = Column(Integer, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    product_valid = Column(Boolean, nullable=False, server_default='false')
    campaign_valid = Column(Boolean, nullable=False, server_default='false')

    def __repr__(self):
        return f"<CleanCoupon(coupon_upc={self.coupon_upc}, product_id={self.product_id}, campaign_id={self.campaign_id})>"