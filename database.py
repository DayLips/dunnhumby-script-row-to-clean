from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(
    os.getenv("DATABASE_URL"),
    connect_args={'options': '-csearch_path=clean'},
    pool_size=10,
    max_overflow=20,
    pool_pre_ping=True
)

class Base(DeclarativeBase):
    ...

from models import CleanTransactionData, CleanCampaignDesc, CleanCampaignTable, CleanCoupon, CleanCouponRedempt, CleanHHDemographic, CleanProduct

def init_db():
    Base.metadata.create_all(bind=engine)