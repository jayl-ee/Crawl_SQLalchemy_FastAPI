import json
import aiohttp
import asyncio
from pandas import json_normalize
from pathlib import Path
import os
import sys
import math
import ast
import datetime

### Directory Setting : DB_CONNECT ####################
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(os.path.join(BASE_DIR,'DB_CONNECT'))
sys.path.append(os.path.join(BASE_DIR,'DATA_TABLE'))
from db_connection import DB_CONNECT
from get_connection_config import *
from weather_local_code import *
from table_info import *
from columns import *

#https://at.agromarket.kr/openApi/price/sale.do?serviceKey= ** 61D7A892DCCD44FBABBF59E3C3F4D1C5
# &apiType=json&pageNo= ** 1   &whsalCd=110001&saleDate= **  20230131


class AT_Crawl:

    def __init__(self):

        today = datetime.datetime.now()
        self.today = today.strftime('%Y-%m-%d')
        # self.db_session = db_session

        config = DB_CONFIG()
        # self.URL_tmp = config.get_connection('AT_URL')
        self.first_page = '1'
        self.SERVICE_KEY = config.get_connection('AT_SERVICE_KEY')

        #columns to crawl
        self.crawl_col_list = [ key for key in at_dict.keys()]
        self.table_col_list = [ value for value in at_dict.values()]

    async def get_urls(self, client_session, date):
        urls = [] # this list is to contain multiple url for 1 day, in which link provided is in pages. And use list to use "asyncio.gather"

        # 첫번째 페이지 불러와서 총 페이지 수  계산
        # url = self.URL_tmp.format(SERVICE_KEY=self.SERVICE_KEY, PAGENO=self.first_page, DATE=date)
        url = f'https://at.agromarket.kr/openApi/price/sale.do?serviceKey={self.SERVICE_KEY}&apiType=json&pageNo={self.first_page}&whsalCd=110001&saleDate={date}'
        async with client_session.get(url) as resp1:
            html = await resp1.text()
            json_file = json.loads(html)

            if json_file['status'] == 'success':
                total_data_cnt = json_file['totCnt']
                cur_page_date_cnt = json_file['dataCnt']
                
              
                pages = (total_data_cnt // cur_page_date_cnt) + 1
               

                for page in range(pages):
                    page += 1
                    url_tmp = url = f'https://at.agromarket.kr/openApi/price/sale.do?serviceKey={self.SERVICE_KEY}&apiType=json&pageNo={page}&whsalCd=110001&saleDate={date}'
                    urls.append(url_tmp)

                return urls

            else: 
                print(' ERROR : Something Happened, Check the KEY of JSON file!! ')

    async def get_json2df(self, client_session, url ):
        async with client_session.get(url) as resp2:
            html = await resp2.text()
            json_file = json.loads(html)
            

            if json_file['status']=='success':
                df = json_normalize(json_file['data'])
                df = df.fillna("")
                df = df.sort_index()
                df = df[self.crawl_col_list]
                df.columns = self.table_col_list
                df['crawl_date'] = self.today


                # bulk insert mapping --> list (dict() , dict() )

                bulk_mapper = df.to_dict(orient='records')

                return bulk_mapper
            
    # def load_db(self, all_data):
    #     for data_for_url in all_data:
    #         self.db_session.bulk_insert_mappings(Agriculture_Table, data_for_url)

    #     self.db_session.commit()


    
    async def main(self, date):
        async with aiohttp.ClientSession(
            trust_env=True,
            connector=aiohttp.TCPConnector(ssl=False),
        ) as self.session:

            urls = await asyncio.gather( 
                    *[ self.get_urls(self.session, date) ]#for date in self.daterange]
            )  

            self.all_data = await asyncio.gather(
                    *[ self.get_json2df(self.session, link) for url in urls for link in url ]
            )

        return self.all_data
        
    def run(self, date):
        return asyncio.run(self.main(date))

class Weather_Crawl:

    def __init__(self):

        config = DB_CONFIG()
        
        #columns to crawl
        self.crawl_col_list = [ key for key in weather_dic.keys()]
        self.table_col_list = [ value for value in weather_dic.values()]


        self.URL = f"https://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList"
        self.SERVICE_KEY = config.get_connection('WEATHER_SERVICE_KEY')
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
        }

    async def get_urls(self, client_session, start_date, end_date, code):


        url = f'https://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList{self.SERVICE_KEY}&pageNo=1&numOfRows=999&dataType=json&dataCd=ASOS&dateCd=DAY&startDt={start_date}&endDt={end_date}&stnIds={code}'

        async with client_session.get(url) as resp1:
            html = await resp1.text()
            json_file = json.loads(html)

            if json_file["response"]["header"]["resultMsg"] == 'NORMAL_SERVICE':

                keys = list(json_file["response"].keys())
                
                try:
                    if "body" in keys:
                        # df = pd.DataFrame()
                        df = json_normalize(json_file["response"]["body"]["items"]["item"])
                    
                except Exception as e:
                    print("json to df error", e)

                df = df[self.crawl_col_list]
                df.columns = self.table_col_list
                df = df.replace('', 1e-9)
                df = df.sort_index()
                bulk_mapper = df.to_dict(orient='records') 
                    
                return bulk_mapper
              
            else: 
                print(' ERROR : Something Happened, Check the KEY of JSON file!! ')


    async def main(self, start_date, end_date):
        async with aiohttp.ClientSession(
            trust_env=True,
            connector=aiohttp.TCPConnector(ssl=False),
        ) as self.session:
            
            # local_code_num : list ( 지역별 코드 )
            local_code_num = [ local_num for local_num in local_code.values()]


            all_data = await asyncio.gather( 
                    *[ self.get_urls(self.session, start_date, end_date, code) for code in local_code_num ]
            )  

        return self.all_data
        
    def run(self):
        return asyncio.run(self.main())


if __name__ == '__main__':

    starttime = datetime.datetime.now()
    
    crawl = AT_Crawl(db_session = 'engine')
    agriculture_data = crawl.run('20230201')

    endtime = datetime.datetime.now()

    print('total time', endtime - starttime)