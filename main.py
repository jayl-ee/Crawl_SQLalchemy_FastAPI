from fastapi import FastAPI
from pathlib import Path
import sys
import os
import datetime
import pandas as pd
from tqdm import tqdm
from sqlalchemy import create_engine, inspect

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR,'DB_CONNECT'))
sys.path.append(os.path.join(BASE_DIR,'DATA_TABLE'))
from db_connection import DB_CONNECT
from DATA_TABLE.table_info import *
from Crawler import *

### CONNECTION ##########################################################
app = FastAPI()
db = DB_CONNECT()
engine = db.engine_connect()
sess = db.sessionmaker(engine)
#######################################################################

### Date ###############################################################
FROM = '2023-02-01'
TO = '2023-02-02'

date_range = [ date.strftime('%Y%m%d') for date in pd.date_range(FROM, TO)]
########################################################################




# 농산물 종합 데이터(가락시장)
@app.get("/agriculture_total")
async def get_agriculture_total():

    Mytable = "agriculture_total"
    agriculture_crawler = AT_Crawl()

    # try:
    # 테이블 존재하는지 확인
    if not inspect(engine).has_table(table_name=Mytable):
        Agriculture_Table.__table__.create(engine)
        sess.commit()
    else: print(f'Connected to "{Mytable}"')

    # 데이터 크롤링
    starttime = datetime.datetime.now()
    
    for date in date_range:
            #date = date_range
        agriculture_data = await agriculture_crawler.main(date)

        # crawl.load_db(agriculture_data)
        for list_of_dicts in agriculture_data:
            sess.bulk_insert_mappings(Agriculture_Table, list_of_dicts) # !! list of dict의 key들이 테이블의 열 이름과 동일해야한다.
            
    sess.commit()


    endtime = datetime.datetime.now()
    duration = endtime - starttime
    print(f'Crawling Complete : it took {duration} seconds. ')

    return agriculture_data[0]


    # except:
    #     print(" ERROR ")




  