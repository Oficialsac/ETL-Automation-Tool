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
        for step in steps:
            if not isinstance(step, Step):
                raise ValueError(f"All objects must be instances of Step, but received {type(step)}.")
            step.execute() 
