import os
import json
def createStepConfig(stepName):
    print(f"Creating StepConfig: {stepName} ")
    config_path = os.path.join(os.getcwd(), "statics")
    try:
        with open(os.path.join(config_path,"config.json"),'r') as file:
           config = json.loads(file.read())
           config.update({stepName: {}})
           
        with open(os.path.join(config_path,"config.json"),'w') as file:
            json.dump(config, file)
           
           
    except Exception as e:
        print(f"Could not create a config step key: {e}")