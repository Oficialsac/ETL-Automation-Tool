from datetime import datetime
import pandas as pd
import numpy as np
import os
import warnings
import logging
import pyspark
import json 
import pyodbc

class Step():
    
    def __init__(self):
        self.getlog = logging.getLogger()
        self.config = {}
    
    def _getConfig(self):
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
        config = self._getConfig()
        if self.__class__.__name__ in config["config"].keys():
            return config["config"][self.__class__.__name__]
        else:
            return {}
        
    def getGlobalConfig(self):
        config = self._getConfig()
        if "global" in config["config"].keys():
            return config["config"]["global"]
        else:
            return {}
                
        
    def ejecutar(self):
        """
            Esta clase ejecuta el paso
        """