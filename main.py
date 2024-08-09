from Step import Step
from Sequencer import Sequencer  
import pandas as pd
from controllers.ApiController.ApiController import RunApiServer
import os
import plotly.express as px 
import seaborn as sns
import matplotlib.pyplot as plt

# Initialize an instance of the Orchestrator class
sq = Sequencer()

class ApiStepExample(Step):
    """
    Demonstrates how to configure a simple API server using FastAPI to handle data transformations.

    This example sets up a FastAPI server that allows you to create endpoints for handling and sharing data.

    Usage:
        1. Obtain an instance of the API controller by calling `getApiController()`.
        2. Use the `run` method to start the server.

    Example:
        To create a simple endpoint and run the server:

        ```python
        # Create an instance of ApiStepExample
        api_example = ApiStepExample()
        
        # Define an endpoint
        @api_example.app.get("/hello")
        def get_hello():
            return {"message": "Hello, world!"}
        
        # Run the server
        api_example.run()
        ```

    Attributes:
        - `app`: The FastAPI application instance. Allows you to define routes and endpoints.

    Notes:
        - The `app` attribute provides access to FastAPI decorators and modules for creating routes and endpoints.
        - Ensure that FastAPI and its dependencies are installed and correctly configured.

    Dependencies:
        - FastAPI
        - Uvicorn (for running the server)
    """
    def execute(self):
        api = self.getApiController()  
        
        @api.app.get("/hola")
        def getHola():
            return "hola"
    
    
class DatabaseStepExample(Step):
    """
    Demonstrates how to connect to a MySQL database using SQLAlchemy and execute a SQL query.

    This example uses SQLAlchemy to establish a database connection and perform SQL queries. 

    Usage:
        1. Obtain an instance of the SQLAlchemy engine by calling `self.getSql()`.
        2. Use the engine to execute SQL queries.

    Example:
        To execute a query and print the results:
        
        ```python
        # Create an instance of DatabaseStepExample
        db_example = DatabaseStepExample()
        
        # Execute the query
        db_example.execute()
        ```
        
        By default, the `execute` method runs a query:
        
        ```python
        print(sql_engine.query("SELECT * FROM accion"))
        ```

    Notes:
        - Ensure that your database configuration is correctly set up.
        - Make sure the SQLAlchemy engine is properly configured to connect to your MySQL database.
        - Replace `"SELECT * FROM accion"` with any SQL query relevant to your application.
        
    Dependencies:
        - SQLAlchemy
        - PyMySQL (for MySQL database connections)
    """
    
    def execute(self):
        sql_engine = self.getSql()
        print(sql_engine.query("SELECT * FROM accion"))
        
class LoadStepData(Step):
    
    def execute(self):
        try:
            filesPath = os.path.join(os.getcwd(),"statics", "files", "archive")
            data_dict = {}
            if len(os.listdir(filesPath)) > 1:
                for data in os.listdir(filesPath):
                    if data.endswith(".csv"):
                        df_name = "_".join(("".join(data.lower().split(".")[:-1])).split(" "))
                        df = pd.read_csv(os.path.join(filesPath, data))
                        data_dict[df_name] = df
                        
                self.setData(data_dict)
        except Exception as e:
            print(f"Error {e}")
            
class ExploratoryAnalysis(Step):
    
    def basicPlotting(self, data):
        
        for column in data.columns:
            if data[column].dtype != 'object':
                # print(f"Column {column}")
                plotData = data
                
                plt = px.histogram(plotData, x=column)
                plt.show()
    
    def execute(self):
        df = self.getData()['data']   
        
        df = df['depression_data']
        print(df.describe())
        self.basicDataInformation(df)
        
        self.basicPlotting(df)
    

if __name__ == '__main__':
    
    sq.run(
        [
            LoadStepData(),
            ExploratoryAnalysis()
        ]
    )