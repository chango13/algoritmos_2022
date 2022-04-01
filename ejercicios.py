#ejercicio 2: Implementar una función que calcule la suma de todos los números enteros comprendidos
#entre cero y un número entero positivo dado.
from ctypes import sizeof


def suma_intervalo(num):
    
    if(num == 0):
        return num
    else:
        return  num + suma_intervalo(num-1)
        


print(suma_intervalo(10))


#Ejercicio 4: Implementar una función para calcular la potencia dado dos números enteros, el primero re-
#presenta la base y segundo el exponente.
def potencia(base, exponente):
    if(exponente == 0):
        return 1
    else:
        return base * potencia(base, exponente-1)


print(potencia(3,4))




#Ejercicio 6: Dada una secuencia de caracteres, obtener dicha secuencia invertida.
cadena = 'hola'
def invertir(cadena, indice):
    if(indice==1):
        return cadena[indice-1]
    else:
        return cadena[indice-1] + invertir(cadena, indice-1)
        #return cadena[-1] + invertir(cadena, indice-1)



def invertir2(cadena):
    if(len(cadena)==0):
        return cadena
    else:
        return cadena[-1] + invertir2(cadena[:-1])
        #return cadena[-1] + invertir(cadena, indice-1)


print(invertir(cadena, len(cadena)))

print(invertir2(cadena))



#Ejercicio 7: Desarrollar un algoritmo que permita calcular la siguiente serie: 1+1/2+1/3+1/4+...+1/n
def sumatoria(numero):
    if(numero == 1):
        return numero
    else:
        return 1/numero + sumatoria(numero-1)


print(sumatoria(5))


#ejercicio 10: Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero.
def contador(numero):
    if(numero < 10):
        return 1
    else:
        return 1 + contador(numero//10)


print(contador(90489))

#ejercicio 20: Desarrollar un algoritmo que permita implementar la búsqueda secuencial con centinela de
#manera recursiva, y permita determinar si un valor dado está o no en dicha lista.
vec = [1, 3, 4, 5, 70, 100]

def buscar(vector, buscado, indice):
    if(indice==len(vector)):
        return -1
    elif(buscado == vector[indice]):
        return indice
    else:
        return buscar(vector, buscado, indice +1)



def busqueda_sec(vector, buscado):
    if(len(vector)==0):
        return -1
    elif(buscado == vector[-1]):
        return len(vector)-1
    else:
        return busqueda_sec(vector[:-1], buscado)


def busqueda_binaria(vector, buscado, primero, ultimo):
        med = (primero + ultimo) // 2
        if(primero > ultimo):
            return -1
        if(buscado == vector[med]):
            return med
        elif(vector[med] < buscado):    
              busqueda_binaria(vector, buscado, med + 1, ultimo)
        else:
               busqueda_binaria(vector, buscado, primero, med - 1)


print(buscar(vec, 71, 0))
print(busqueda_sec(vec, 70))
print("Posicion: ", busqueda_binaria(vec, 4, 0, len(vec)-1))