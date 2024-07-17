# This controller will be used to deploy a local server with Fast Api
# and simple routes to use
import os
from typing import Union, Dict, Callable
from fastapi import FastAPI
import uvicorn
from utils.getConfig import Config

__config = Config()
app = FastAPI()

class RunApiServer():
    def __init__(self, server_name, **kwargs):
        self.server_name = server_name
        self.params = kwargs

    def getApiTemplate(self):
        path = os.path.join(os.getcwd(),"controllers","statics")
        print(os.listdir(path))
        # with open(r"C:\Users\Steve\Documentos\orquestador\controllers\ApiController.py", "r") as f:
        #     return f.read()
    
    def run(self):
        
        self.getApiTemplate()
        # self.createRoute(routes_config)
        
        # uvicorn.run(app, host="127.0.0.1", port=8080)
        
        
        
    