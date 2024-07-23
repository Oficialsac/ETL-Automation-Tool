import os
import json
from Step import Step

class Orchestrator:
    """
    Orchestrator class that manages and executes a sequence of steps.
    """
    
    def __init__(self):
        """
        Initializes an instance of the Orchestrator class.
        """
        self._steps = []  # List to store steps
        
    def run(self, steps):
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
                host = input("Enter the database host (default localhost): ") or "localhost"
                port = input("Enter the database port (default 3306): ") or "3306"
                user = input("Enter the database user: ")
                password = input("Enter the database password: ")
                database = input("Enter the database name: ")
                
                config_dict["global"] = {
                    "host": host,
                    "port": port,
                    "user": user,
                    "password": password,
                    "database": database
                }
                
                with open(os.path.join(config_path,"config.json"), "w") as file:
                    json.dump(config_dict, file)
                    
            else:
                for step in steps:
                    if not isinstance(step, Step):
                        raise ValueError(f"All objects must be instances of Step, but received {type(step)}.")
                    step.execute()
        except Exception as e:
            print(f"Error executing: {e}")
