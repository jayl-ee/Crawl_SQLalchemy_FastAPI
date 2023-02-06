import json
from pathlib import Path
import os
import ast



class DB_CONFIG():
    def __init__(self):
        BASE_DIR = Path(__file__).resolve().parent
        secret_file = f'{BASE_DIR}/secrets.json'

        ## Loag JSON
        with open(secret_file) as f:
            self.secrets = json.loads(f.read())

    def get_connection( self,  key: str ):

            try:
                return self.secrets[key]
            except:
                print('Please Check If you have a json file or check if your KEY exist in json file.')    




#config = DB_CONFIG()

#AT_SERVICE_KEY = config.get_connection('AT_SERVICE_KEY')

if __name__ == '__main__':

    config = DB_CONFIG()
    
    print(f"You are in {__name__} !!" )
    print('\n')
    print(f"     SAMPLE RESULT : POSTGRES_ID ==> {config.get_connection('SERVER_NAME')})")

    print(config.get_connection('AT_CRAWL_COLUMNS'))
    a = config.get_connection('AT_CRAWL_COLUMNS')
    a = ast.literal_eval(a)
    a = [n.strip() for n in a]
    for col in a:
        print(col)