from sqlalchemy import Column, Integer, BigInteger, Boolean, PrimaryKeyConstraint
from database import Base

class CleanCouponRedempt(Base):
    __tablename__ = 'coupon_redempt'
    __table_args__ = (
        PrimaryKeyConstraint('household_key', 'day', 'coupon_upc', 'campaign_id'),
        {'schema': 'clean'}
    )

    household_key = Column(BigInteger, nullable=False)
    day = Column(Integer, nullable=False)
    coupon_upc = Column(BigInteger, nullable=False)
    campaign_id = Column(Integer, nullable=False)
    household_valid = Column(Boolean, nullable=False, server_default='false')
    coupon_campaign_valid = Column(Boolean, nullable=False, server_default='false')

    def __repr__(self):
        return f"<CleanCouponRedempt(household={self.household_key}, coupon={self.coupon_upc}, day={self.day})>"