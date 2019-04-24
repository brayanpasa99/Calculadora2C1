from Calculadora import Operaciones


class Principal():

    def principal(self, ):

        pila = []
        resultado = 0

        while True:

            cadena = ""

            print("CALULADORA NOTACION POLACA INVERSA")

            print("\nPILA DE DATOS:")

            for i in range(0, len(pila)):
                cadena = cadena + (str(pila[i])+" ")
            print (cadena)

            elemento = raw_input(": ")

            if elemento == "+":
                if len(pila)>=2:
                    resultado = Operaciones.Operaciones().suma(pila[len(pila)-2], pila[len(pila)-1])
                    pila.pop()
                    pila[len(pila)-1] = resultado
                else:
                    print ("Argumentos insuficientes")

            elif elemento == "-":
                if len(pila)>=2:
                    resultado = Operaciones.Operaciones().resta(pila[len(pila)-2], pila[len(pila)-1])
                    pila.pop()
                    pila[len(pila)-1] = resultado
                else:
                    print ("Argumentos insuficientes")

            elif elemento == "*":
                if len(pila)>=2:
                    resultado = Operaciones.Operaciones().multiplicacion(pila[len(pila)-2], pila[len(pila)-1])
                    pila.pop()
                    pila[len(pila)-1] = resultado
                else:
                    print ("Argumentos insuficientes")

            elif elemento == "/":
                if len(pila)>=2:
                    resultado = Operaciones.Operaciones().division(pila[len(pila)-2], pila[len(pila)-1])
                    pila.pop()
                    pila[len(pila) - 1] = resultado
                else:
                    print ("Argumentos insuficientes")

            elif elemento == "sig":
                if len(pila)>=1:
                    pila[len(pila) - 1] = Operaciones.Operaciones().signo(pila[len(pila)-1])
                else:
                    print ("Argumentos isuficientes")

            elif elemento == "o":
                Operaciones.Operaciones().radixSort(pila)

            elif elemento == "s":
                exit()

            elif elemento.isalpha():
                print ("No puedo interpretar la funcion indicada")

            elif float(elemento):
                pila.append(elemento)

