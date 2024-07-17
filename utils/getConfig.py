import os 
import json

class Config():
    def __init__(self):
        self.config = {}
        
    def getConfig(self):
        """
        Retrieves the configuration from a JSON file located in the 'statics' directory.

        Returns:
            dict: The configuration dictionary.
        """
        configPath = os.path.join(os.getcwd(), 'statics')  
        print(os.listdir(configPath))  
        if "config.json" in os.listdir(configPath): 
            with open(configPath + "/config.json", 'r') as f: 
                self.config["config"] = json.load(f)  
                
        if len(self.config.values()) != 0: 
            return self.config
        else:
            return {}