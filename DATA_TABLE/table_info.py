from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Agriculture_Table(Base):
    __tablename__ = 'agriculture_total'

    id = Column(Integer, primary_key=True,autoincrement=True )
    saleDate = Column(DateTime)
    market_name = Column(String)
    market_code = Column(Integer)
    item = Column(String)
    min_price = Column(Float)
    max_price = Column(Float)
    avg_price = Column(Float)
    crawl_date = Column(DateTime)