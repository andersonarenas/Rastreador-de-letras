# script que busca una letra de una palabra o frase y la imprime, usado para fines de estudio y practica

# primero pedimos la palabra o frase al usuario, y la letra que va a buscar

palabra = input("Ingrese su palabra o frase: ")
letra = input("Ingrese la letra que desea buscar: ")

# se genera un ciclo for para que recorra la frase o palabra en busqueda de la letra designada

for i in palabra:
    # el ciclo if es el que indica cuando se encuentra la letra e imprime el mensaje
    if i == letra:
        print("Se encontro la letra {}".format(letra))
        break
    else:
        print("no se encontro la letra seleccionada")
        break
