from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from utils.getConfig import Config
from utils.updateConfig import updateConfig
import pandas as pd
import json
import os

class SqlController():
    def __init__(self):
        self.connection = self.__connect()
        
    def query(self, query: str):
        engine = self.connection
        try:
            return pd.read_sql(query, engine)
        except Exception as e:
            print(f"Error executing query: {e}")
            raise
            
    def create_table(self, nametable):
        pass
    
    def __database_config(self,__config):
        host = input("Enter the database host (default localhost): ") or "localhost"
        port = input("Enter the database port (default 3306): ") or "3306"
        user = input("Enter the database user: ")
        password = input("Enter the database password: ")
        database = input("Enter the database name: ")
        
        database_config = {
                "database": {
                    "host": host,
                    "port": port,
                    "user": user,
                    "password": password,
                    "database": database
                }
            }
        
        updateConfig(database_config)
        
    
    def __connect(self):
        try:
            __config = Config()
            
            if  "database" not in __config.getConfig()["config"].keys():
                self.__database_config(__config)
            
            config = __config.getConfig()["config"]["database"]
            
            SQL_ALCHEMY_DATABASE_URL = (
                f"mysql+pymysql://{config['user']}:{config['password']}@"
                f"{config['host']}:{config['port']}/{config['database']}"
            )

            engine = create_engine(
                SQL_ALCHEMY_DATABASE_URL
            )
            
            return engine

        except pymysql.err.OperationalError as e:
            if e.args[0] == 1045:
                print("Error: Access denied for user 'root'@'localhost' (using password: YES)")
            elif e.args[0] == 2003:
                print("Error: Can't connect to MySQL server on 'localhost' (MySQL server may be down)")
            else:
                print(f"OperationalError: {e}")
        except pymysql.err.InternalError as e:
            print(f"InternalError: {e}")
        except pymysql.err.ProgrammingError as e:
            print(f"ProgrammingError: {e}")
        except pymysql.err.IntegrityError as e:
            print(f"IntegrityError: {e}")
        except pymysql.err.DataError as e:
            print(f"DataError: {e}")
        except pymysql.err.NotSupportedError as e:
            print(f"NotSupportedError: {e}")
        except pymysql.err.DatabaseError as e:
            print(f"DatabaseError: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")