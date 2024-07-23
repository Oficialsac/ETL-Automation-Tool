from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from utils.getConfig import Config
import pandas as pd

class SqlController():
    def __init__(self):
        self.connection = self.__connect()
        
    def query(self, query: str):
        return pd.read_sql(query, self.connection)
    
    def create_table(self, nametable):
        pass
        
    def __connect(self):
        try:
            __config  = Config()
            config = __config.getConfig()["config"]
            
            SQL_ALCHEMY_DATABASE_URL = f"mysql+pymysql://{config['global']['user']}:{config['global']['password']}@{config['global']['host']}:{config['global']['port']}/{config['global']['database']}"

            engine = create_engine(
                SQL_ALCHEMY_DATABASE_URL
            )
            
            Session = sessionmaker(bind=engine)
            session = engine.connect()
            Base = declarative_base()
            
            return session
        except Exception as e:
            print(f"Error {e}")