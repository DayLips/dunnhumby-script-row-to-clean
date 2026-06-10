from sqlalchemy import Column, Integer, String
from database import Base

class CleanCampaignDesc(Base):
    __tablename__ = 'campaign_desc'
    __table_args__ = {'schema': 'clean'}

    campaign = Column(Integer, primary_key=True, index=True)
    campaign_type  = Column(String(1), nullable=True) 
    start_day = Column(Integer, nullable=False)
    end_day = Column(Integer, nullable=False)
    campaign_duration_days = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<CleanCampaignDesc(campaign={self.campaign}, type='{self.description}')>"