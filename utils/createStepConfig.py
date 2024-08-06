import os
import json
def createStepConfig(stepName):
    try:
        config_path = os.path.join(os.getcwd(), "statics")
        if "config.json" in os.listdir(config_path):
            with open(os.path.join(config_path,"config.json"),'r') as file:
                config = json.loads(file.read())
                if stepName not in config.keys():
                    config.update({stepName: {}})
                    print(f"Configuration for {stepName} successfully updated")
                
            with open(os.path.join(config_path,"config.json"),'w') as file:
                json.dump(config, file)
                
           
    except Exception as e:
        print(f"Could not create a config step key: {e}")