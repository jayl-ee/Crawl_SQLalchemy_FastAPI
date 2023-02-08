# API Crawling - Fast API & SQL alchemy

this repository provides code to crawl from API and insert into database
In order to use this code, you MUST get the SERVICE KEY to access the API.

The link for the API I used is below...


```bash
 ┣ DATA_TABLE
 ┃ ┣ columns.py
 ┃ ┣ create_table.py
 ┃ ┣ table_info.py
 ┃ ┗ weather_local_code.py
 ┣ DB_CONNECT
 ┃ ┣ db_connection.py
 ┃ ┣ get_connection_config.py
 ┃ ┗ secrets.json
 ┣ Crawler.py
 ┣ README.md
 ┣ main.py
 ┣ requirements.txt
 ┣ server.py
 ┗ test_crawl.ipynb
```




## Database Platform

- PostgresSQL

## Crawl API

- AT 도매시장 통합 홈페이지 : https://at.agromarket.kr
- 공공데이터 포털 (기상청) : https://www.data.go.kr/tcs/dss/selectDataSetList.do?dType=API&keyword=기상청

## requirements.txt
aiohttp==3.8.3
SQLAlchemy==1.4.39
asyncio==3.4.3
uvicorn==0.20.0
```



### 📁code

* #### Crawler.py | Async Programming
- get json from API
- use async to insert into Database

* #### main.py
- main file to run in Fast API

* #### columns.py
- dictionary to transform column name
- fornmat : { API COLUMN NAME : DB COLUMN NAME}

* #### create_table.py
- example python file to create table in Database

* #### table_info.py
- define table
- same as "CREATE TABLE ** " SQL language

* #### db_connection.py
- connect database server

* #### get_connection_config.py
- function to get API Key, DB url, secret keys etc.


##### uvicorn
```python
import uvicorn

def start():
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

if __name__ == "__main__":
    start()
```