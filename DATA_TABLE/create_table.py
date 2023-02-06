from pathlib import Path
import sys
import os
import argparse
from sqlalchemy import create_engine, inspect

'''
In Command Window, to create table type...

=> python create_table.py --table_name=(TABLE_NAME) <=

'''

### Table #############################################
from table_info import *


### Directory Setting : DB_CONNECT ####################
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(os.path.join(BASE_DIR,'DB_CONNECT'))
from db_connection import DB_CONNECT


### Choose Table Name You want to CREATE #########@@@@@
parser = argparse.ArgumentParser()
parser.add_argument('--table_name', type=str)
parsers = parser.parse_args()
########################################################



if __name__ == '__main__':

    db = DB_CONNECT()
    engine = db.engine_connect()
    sess = db.sessionmaker(engine)
   
    if parsers.table_name == "agriculture_total":
        if not inspect(engine).has_table(table_name=f'{parsers.table_name}'):
            Agriculture_Table.__table__.create(engine)
            sess.commit()
            print(" TABLE Created ")
        else: 
            sess.close()
            print(' [ agriculture_total ] exists in your DB')