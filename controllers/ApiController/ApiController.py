# This controller will be used to deploy a local server with Fast Api
# and simple routes to use
from fastapi import FastAPI, Depends
from fastapi.responses import *
import uvicorn
from utils.getConfig import Config
from ListNode.List import List

app = FastAPI()

class RunApiServer():
    
    global __config, __list
    __config = Config()
    __list = List()
    
    def __init__(self, server_name, **kwargs):
        self.server_name = server_name
        self.params = kwargs
        self.etls = {}
        self.app = app

    def setApiData(self, data):
        if not __list.isEmpty():
            __list.deleteNode()
        __list.addFirst(data)
        
    @app.get('/')
    async def __getSwaggerPath():
        response = RedirectResponse(url="/docs")
        return response
        
    def run(self):
        try: 
            uvicorn.run(app, host="127.0.0.1", port=8080)
        except Exception as e:
            print(f"Error running uvicorn: {e}")
        
        
    