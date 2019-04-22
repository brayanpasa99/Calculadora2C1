class Operaciones():

    def __init__(self):
        pass

    def suma(self, val1, val2):
        return float(val1) + float(val2)

    def resta(self, val1, val2):
        return float(val1) - float(val2)

    def multiplicacion(self, val1, val2):
        return float(val1) * float(val2)

    def division(self, val1, val2):
        return float(val1) / float(val2)

    def signo(self, val):
        return str(float(val)*-1)
