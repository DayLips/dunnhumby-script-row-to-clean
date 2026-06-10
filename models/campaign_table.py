from sqlalchemy import Column, Integer, String, BigInteger
from database import Base

class CleanCampaignTable(Base):
    __tablename__ = 'campaign_table'
    __table_args__ = {'schema': 'clean'}

    household_key = Column(BigInteger, primary_key=True, nullable=False)
    campaign_id = Column(Integer, primary_key=True, nullable=False)
    campaign_type = Column(String(1), nullable=True)

    def __repr__(self):
        return f"<CleanCampaignTable(household={self.household_key}, campaign={self.campaign_id}, type={self.campaign_type})>"