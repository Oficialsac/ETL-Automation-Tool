from datetime import datetime
import pandas as pd
import numpy as np
import os
import warnings
import logging
from pyspark.sql import SparkSession
import json 
import pyodbc
from ListNode.List import List

class Step():
    global __list
    __list = List()
    print("HAOL CASDASFA")
    def __init__(self):
        self.getlog = logging.getLogger()
        self.config = {}
        self.__dataToPass = {}
        
    
    def __getConfig(self):
        configPath = os.path.join(os.getcwd(), 'statics')
        print(os.listdir(configPath))
        if "config.json" in os.listdir(configPath):
            with open(configPath+"\config.json", 'r') as f:
                self.config["config"] = json.load(f)
                
        if len(self.config.values()) != 0:
            return self.config
        else:
            return {}
        
    def getStepConfig(self):
        config = self.__getConfig()
        if self.__class__.__name__ in config["config"].keys():
            return config["config"][self.__class__.__name__]
        else:
            return {}
        
    def getGlobalConfig(self):
        config = self.__getConfig()
        if "global" in config["config"].keys():
            return config["config"]["global"]
        else:
            return {}
    
    def setData(self, data):
        self.__dataToPass["data"] = data
        if __list.isEmpty() == False:
            __list.deleteNode()
        __list.addFirst(self.__dataToPass)
        
    def getData(self):
        if __list.count() != 0:
            return __list.getData()
        