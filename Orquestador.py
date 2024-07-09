from Step import Step
class Orquestador():
    def __init__(self):
        self._steps = []
        
    def Run(self, steps):
        for step in steps:
            if not isinstance(step, Step):
                raise ValueError(f"Todos los objetos deben ser instancias de Step, pero se recibió {type(step)}.")
            step.ejecutar()
    
        