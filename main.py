#Funciones que hicimos en clearn

def cantidad_de_digitos(numero):
    contador = 0
    while numero != 0:
        numero = numero//10
        contador += 1
    return contador

def en_posicion(numero, indice, reversa):
    contador = 0
    if reversa == True:
        while contador != indice:
            numero= numero//10
            contador += 1
        numero = numero%10
        return numero
    else:
            largo = cantidad_de_digitos(numero)
            numero = numero%10**(largo-indice)
            n = cantidad_de_digitos(numero)
            numero = numero//10**(n-1)
            return numero


def reemplazar(numero, indice, nuevo, reversa):
    contador = 0
    if reversa == True:
        while en_posicion(numero, indice, reversa) != nuevo:
            if en_posicion(numero, indice, reversa) > nuevo:
                numero = numero-10**indice
            else:
                numero = numero+10**indice
        return numero
    else:
        largo = cantidad_de_digitos(numero)-1
        ceros = largo-indice
        while en_posicion(numero, indice, reversa) != nuevo:
            if en_posicion(numero, indice, reversa) > nuevo:
                numero = numero-10**ceros
            else:
                numero = numero+ 10**ceros
        return numero
