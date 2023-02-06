from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker, declarative_base

from get_connection_config import DB_CONFIG


class DB_CONNECT():
    def __init__(self):
        config = DB_CONFIG()

        self.db = config.get_connection('DB')
        self.server_name = config.get_connection('SERVER_NAME')
        self.port = config.get_connection('PORT')
        self.db_name = config.get_connection('DB_NAME')
        self.id = config.get_connection('POSTGRES_ID')
        self.pw = config.get_connection('POSTGRES_PSSD')

    
    def engine_connect(self):
        
        self.DB_URL = f"{self.db}://{self.id}:{self.pw}@{self.server_name}:{self.port}/{self.db_name}"
        self.engine = create_engine(self.DB_URL)

        return self.engine
        
    def sessionmaker(self, engine):
        self.Sess = sessionmaker(bind=engine)
        # self.Sess() 
        session = self.Sess()

        return session





if __name__ == '__main__':
    
    db = DB_CONNECT()
    engine = db.engine_connect()
    sess = db.sessionmaker(engine)

    print( f'session ==>  {sess}')