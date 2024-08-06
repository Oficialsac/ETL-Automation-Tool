import os
import inspect
import logging
import json 
from ListNode.List import List
import utils.getClassParams
from utils.getConfig import Config
from utils.createStepConfig import createStepConfig
import utils 
from controllers.ApiController.ApiController import RunApiServer
from controllers.SqlController.SqlController import SqlController

class Step:
    """
    Step class that manages configuration and data for a specific step in a process.
    Utilizes a global list to store temporary data.
    """
    global __config, __list
    __config = Config()
    __list = List()
    
    def __init__(self):
        """
        Initializes an instance of the Step class.
        """
        self.getlog = logging.getLogger(__name__) 
        self.config = {}
        self.__dataToPass = {}
        self.userInputs = {}
        self.kwarg = {}
                    
        
    def getStepConfig(self):
        """
        Retrieves the configuration specific to the current step.

        Returns:
            dict: The step-specific configuration dictionary.
        """
    
        config = __config.getConfig()  
        if self.__class__.__name__ in config["config"].keys():  
            return config["config"][self.__class__.__name__]
        else:
            return {
                "code": False,
                "error": self.__class__.__name__ + "does not exist in configuration file"
            }
        
    def getGlobalConfig(self):
        """
        Retrieves the global configuration.

        Returns:
            dict: The global configuration dictionary.
        """
        config = __config.getConfig()  
        if "global" in config["config"].keys():  
            return config["config"]["global"]
        else:
            return {}
    
    def setData(self, data):
        """
        Sets data to be passed and stores it in the global list.

        Args:
            data (any): The data to be stored.
        """
        self.__dataToPass["data"] = data  
        if not __list.isEmpty():  
            __list.deleteNode()  
        __list.addFirst(self.__dataToPass) 
        
    def getData(self):
        """
        Retrieves the stored data from the global list.

        Returns:
            any: The data stored in the list, if it exists.
        """
        if __list.count() != 0:  # Check if the list is not empty
            return __list.getData()  # Get the data from the list
        
    def getSql(self):
        return SqlController()
    
    def getApiController(self):
        params = utils.getClassParams.getParameters(RunApiServer)
        params = [param for param in params if param != 'kwargs']
        
        print("To create a new API controller, it is necessary to receive some mandatory parameters to run.")
        
        for param in params:
            while True:
                value = input(f"Please enter a value for the mandatory parameter {param.upper()}: ")
                if value:
                    self.userInputs[param] = value
                    y_n = input("You need to create a specific port? (Y/N)")
                    if y_n.lower() == "y":
                        self.kwarg["port"] = input("Enter the specific port: ")
                        self.userInputs.update(self.kwarg)
                        break
                    else:
                        break
                else:
                    print(f"{param.upper()} is mandatory and cannot be empty.")
        
    
        app = RunApiServer(self.userInputs['server_name'], kwargs=self.kwarg)
        return app
            
            
                

        