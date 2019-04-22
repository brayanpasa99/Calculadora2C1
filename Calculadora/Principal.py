from Calculadora import Operaciones


class Principal():

    def principal(self):

        pila = []
        resultado = 0

        while True:

            print("CALULADORA NOTACION POLACA INVERSA")

            elemento = input(": ")

            if elemento == "+":
                resultado = Operaciones.Operaciones().suma(pila[len(pila)-2], pila[len(pila)-1])
                pila.pop()
                pila[len(pila)-1] = resultado

            elif elemento == "-":
                resultado = Operaciones.Operaciones().resta(pila[len(pila)-2], pila[len(pila)-1])
                pila.pop()
                pila[len(pila)-1] = resultado

            elif elemento == "*":
                resultado = Operaciones.Operaciones().multiplicacion(pila[len(pila)-2], pila[len(pila)-1])
                pila.pop()
                pila[len(pila)-1] = resultado

            elif elemento == "/":
                resultado = Operaciones.Operaciones().division(pila[len(pila)-2], pila[len(pila)-1])
                pila.pop()
                pila[len(pila) - 1] = resultado

            elif elemento == "sig":
                pila[len(pila) - 1] = Operaciones.Operaciones().signo(pila[len(pila)-1])

            elif elemento.isalpha():
                pass

            elif float(elemento):
                pila.append(elemento)


            for i in range(0, len(pila)):
                print (pila[i])
