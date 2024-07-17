import inspect
def getParameters(cls):
    rs = inspect.signature(cls.__init__)
    params = rs.parameters
    param_name = [name for name, param in params.items() if name != 'self']
    return param_name 