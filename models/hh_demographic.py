from sqlalchemy import Column, Integer, String, Boolean, BigInteger
from database import Base

class CleanHHDemographic(Base):
    __tablename__ = 'hh_demographic'
    __table_args__ = {'schema': 'clean'}

    household_key = Column(BigInteger, primary_key=True, index=True)
    age_desc = Column(String(20), nullable=True)
    marital_status = Column(String(10), nullable=True)
    income_desc = Column(String(50), nullable=True)
    homeowner_desc = Column(String(30), nullable=True)
    hh_comp_desc = Column(String(50), nullable=True)
    household_size_desc = Column(String(10), nullable=True) 
    kid_category_desc = Column(String(30), nullable=True)    
    
    household_size_numeric = Column(Integer, nullable=True)
    has_kids = Column(Boolean, nullable=True)
    is_retired = Column(Boolean, nullable=True)

    def __repr__(self):
        return f"<CleanHHDemographic(household_key={self.household_key}, age='{self.age_desc}')>"