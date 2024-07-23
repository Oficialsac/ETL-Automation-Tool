from Step import Step
from Orchestrator import Orchestrator  
import pandas as pd
from controllers.ApiController.ApiController import RunApiServer

# Initialize an instance of the Orchestrator class
orchestrator = Orchestrator()

class Tokenization(Step):
    """
    Tokenization class that inherits from Step and implements the execute method.
    This class reads a CSV file and sets the first two rows and column names as data.
    """
    def execute(self):
        """
        Reads data from a CSV file specified in the step configuration and sets it for the next step.
        """
        sql = self.getSql()
        
        df2 = pd.read_csv(r"C:\Users\Steve\Documentos\orquestador\statics\files\us-patent-phrase-to-phrase-matching\train.csv")
        df2.to_sql("hola2", sql.connection, if_exists="append")
        print(sql.query("select * from hola2"))
        
        
        

class Tokenization2(Step):
    """
    Tokenization2 class that inherits from Step and implements the execute method.
    This class prints the data set by the previous step.
    """
    def execute(self):
        """
        Prints the columns and data set by the previous step.
        """
        print("Columns and data necessary for this step:", self.getData()["data"]) 

if __name__ == '__main__':
    # Run the orchestrator with a sequence of steps
    
    orchestrator.run(
        [
            Tokenization(), 
        ]
    )
    
    # with open(r"C:\Users\Steve\Documentos\orquestador\controllers\ApiController.py", "r") as f:
    #     contenido = f.read()
    
    # print(contenido)
    # routesFolderPath = r"C:\Users\Steve\Documentos\orquestador\controllers\routes"
    # for route in ["demo", "demo2"]:
    #     with open(routesFolderPath+f"\{route}_route.py", "w") as f:
    #         f.write(contenido)