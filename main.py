from Step import Step
from Orquestador import Orquestador
import pandas as pd
orquestador = Orquestador()
class Tokenizacion(Step):
    def ejecutar(self):
        dataPath = self.getStepConfig()["dataPath"][0] + "/test.csv"
        df = pd.read_csv(dataPath)
        self.setData([df.iloc[0:2], df.columns.to_list()])
        
class Tokenizacion2(Step):
    def ejecutar(self):
        print("Columnas y datos necesarios para este paso", self.getData()["data"]) 
        
if __name__ == '__main__':
    orquestador.Run(
        [
            Tokenizacion(), 
            Tokenizacion2(), 
         ])
    