import os
import json
from Step import Step
import datetime
import inspect
from utils.createStepConfig import createStepConfig
class Orchestrator:
    """
    Orchestrator class that manages and executes a sequence of steps.
    """
    
    def __init__(self):
        """
        Initializes an instance of the Orchestrator class.
        """
        self._steps = []  # List to store steps
        
    def validateInitialization(self):
        for step in self._steps:
            createStepConfig(step.__class__.__name__)
            if not isinstance(step, Step):
                raise ValueError(f"All objects must be instances of Step, received {type(step)}.")
                    
            if True in [True if "execute" in item[0] else False if inspect.ismethod(item[1]) else None for item in inspect.getmembers(step)]:
                step.execute()
            else:
                print(f"Does not exist in step: {step.__class__.__name__} a method 'execute' necessary to run the orchestrator")
        
    def run(self, steps):
        
        self._steps = steps
        """
        Executes each step in the provided list of steps.

        Args:
            steps (list): A list of Step instances to be executed.

        Raises:
            ValueError: If any object in the list is not an instance of Step.
        """
        config_path = os.path.join(os.getcwd(), "statics")
        config_dict = {"config": {}}
        try:
            if "config.json" not in os.listdir(config_path):
                author = input("Enter your author name: ")
                project_name = input("Enter the name of your project: ") 
                
                config_dict["config"].update({"global":{
                    "author": author,
                    "project_name": project_name,
                    "date": str(datetime.datetime.now())
                    }
                })
                
                with open(os.path.join(config_path,"config.json"), "w") as file:
                    json.dump(config_dict, file)
                
                self.validateInitialization()
            else:
                self.validateInitialization()
                    
        except Exception as e:
            print(f"Error executing: {e}")
