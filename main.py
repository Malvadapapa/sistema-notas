from src.calculadora_promedios import Calculadora_promedios



calculadora = Calculadora_promedios()


def menu ():

    notas = []

    print("***bienvenido, ingrese 3 numeros para calcular su promedio***")
    for i in range(3):
        valor = int(input(f"ingrese la nota {i+1}:"))
        notas.append(valor)

    print(f"Su promedio es: {calculadora.calcular_promedio(notas[0], notas[1], notas[2])}")
    
    #print(f"Su promedio es: {calculadora.calcular_promedio(notas)}")


menu()