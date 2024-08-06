import json
import os


def updateConfig(dictionary):
    config_path = os.path.join(os.getcwd(), "statics")
    
    with open(os.path.join(config_path,"config.json"),'r') as file:
        config = json.loads(file.read())
        config.update(dictionary)
                
    with open(os.path.join(config_path,"config.json"),'w') as file:
        json.dump(config, file)
    