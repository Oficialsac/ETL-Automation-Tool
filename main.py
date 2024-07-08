from Step import Step

class Tokenizacion(Step):
    def ejecutar(self):
        return [self.getStepConfig(), self.getGlobalConfig()]
        
        
if __name__ == '__main__':
    StepUno = Tokenizacion()
    configuracion_del_paso = StepUno.ejecutar()
    print(configuracion_del_paso)
    