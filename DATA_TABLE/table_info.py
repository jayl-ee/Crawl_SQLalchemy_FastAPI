from sqlalchemy import Column, String, Integer, DateTime, Float , Numeric, Identity, null, Sequence
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


class Weather(Base):
    __tablename__ = "weather"

    id = Column(Integer, autoincrement=True, primary_key=True)
    date = Column(String(20), nullable=False)  # 날짜
    state_id = Column(String(20), nullable=True)  # 지점번호
    state = Column(String(50), nullable=True)  # 지점명

    avg_temp = Column(Numeric, nullable=True) # 평균기온
    min_temp = Column(Numeric, nullable=True) # 최저기온
    min_temp_time = Column(String(20), nullable=True)  # 최저기온 시각
    max_temp = Column(Numeric, nullable=True) # 최고기온
    max_temp_time = Column(String(20), nullable=True)  # 최고기온 시각

    rain_dur_time = Column(Numeric, nullable=True) # 강수 계속 시간
    min10_max_rain = Column(Numeric, nullable=True) # 10분 최다 강수량
    min10_max_rain_time = Column(String(20), nullable=True) # 10분 최다 강수량 시각(hhmi)
    hour1_max_rain = Column(Numeric, nullable=True) # 1시간 최다 강수량
    hour1_max_rain_time = Column(String(20), nullable=True) # 1시간 최다 강수량 시각(hhmi)
    rain_all_day = Column(Numeric, nullable=True) # 일강수량(mm)

    max_ins_wind_speed = Column(Numeric, nullable=True) # 최대 순간 풍속
    max_ins_wind_speed_dir = Column(Integer, nullable=True) # 최대 순간 풍속 풍향(16방위)
    max_ins_wind_speed_time = Column(String(20), nullable=True) # 최대 순간 풍속 시각(hhmi)
    max_wind_speed = Column(Numeric, nullable=True) # 최대 풍속
    max_wind_speed_dir = Column(Integer, nullable=True) # 최대 풍속 풍향(16방위)
    max_wind_speed_time = Column(String(20), nullable=True) # 최대 풍속 시각(hhmi)
    avg_wind_speed = Column(Numeric, nullable=True) # 평균풍속
    hr24_sum_rws = Column(Integer, nullable=True) # 풍정합
    max_wind = Column(Integer, nullable=True) # 최다 풍향

    ave_dew_point_temp = Column(Numeric, nullable=True) # 평균 이슬점 온도(c)

    min_moisture = Column(Numeric, nullable=True) # 최소 상대습도
    min_moisture_time = Column(String(20), nullable=True) # 평균 상대습도 시각
    avg_moisture = Column(Numeric, nullable=True) # 평균 상대습도

    avg_pressure = Column(Numeric, nullable=True) # 평균 증기압
    avg_pressure_at = Column(Numeric, nullable=True) # 평균 현지기압
    max_pressure_sea = Column(Numeric, nullable=True) # 최고 해면 기압
    max_pressure_sea_time = Column(String(20), nullable=True) # 최고 해면기압 시각
    min_pressure_sea = Column(Numeric, nullable=True) # 최저 해면기압
    min_pressure_sea_time = Column(String(20), nullable=True) # 최저 해면기압 시각
    avg_pressure_sea = Column(Numeric, nullable=True) # 평균 해면기압

    dur_sun = Column(Numeric, nullable=True) # 가조 시간
    sum_sun_hour = Column(Numeric, nullable=True) # 합계 일조 시간
    hr1_max_time = Column(String(20), nullable=True) # 1시간 최다 일사 시각
    hr1_max_rate = Column(Numeric, nullable=True) # 1시간 최다 일사량
    sum_sun = Column(Numeric, nullable=True) # 합계 일사량

    day_snow = Column(Numeric, nullable=True) # 일 최심적설
    day_snow_new = Column(Numeric, nullable=True) # 일 최심신적설
    avg_cloud = Column(Numeric, nullable=True) # 평균 전운량(10분위)
    avg_ground_temp = Column(Numeric, nullable=True) # 평균 지면온도