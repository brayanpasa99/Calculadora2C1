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

    def buscar(self, lista, val):

        for i in range(len(lista)):
            if lista[i] == val:
                print('Elemento encontrado en la posicion: ', i)
                print("")

    def ordenamientoPorMezcla(self, unaLista):
        if len(unaLista)>1:
            mitad = len(unaLista)//2
            mitadIzquierda = unaLista[:mitad]
            mitadDerecha = unaLista[mitad:]

            self.ordenamientoPorMezcla(mitadIzquierda)
            self.ordenamientoPorMezcla(mitadDerecha)

            i=0
            j=0
            k=0
            while i < len(mitadIzquierda) and j < len(mitadDerecha):
                if mitadIzquierda[i] < mitadDerecha[j]:
                    unaLista[k]=mitadIzquierda[i]
                    i=i+1
                else:
                    unaLista[k]=mitadDerecha[j]
                    j=j+1
                k=k+1

            while i < len(mitadIzquierda):
                unaLista[k]=mitadIzquierda[i]
                i=i+1
                k=k+1

            while j < len(mitadDerecha):
                unaLista[k]=mitadDerecha[j]
                j=j+1
                k=k+1
