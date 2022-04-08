#5-Desarrollar una función que permita convertir un número romano en un número decimal.

def conversion(romano):
        num_romanos = {'I': 1.0, 'V': 5.0, 'X':10.0, 'L': 50.0, 'C': 100.0, 'D': 500.0, 'M': 1000.0}
        dec = 0
        for i in range(len(romano)):
                if i == 0 or num_romanos[romano[i]] <= num_romanos[romano[i - 1]]:
                        dec += num_romanos[romano[i]]
                elif i > 0 and num_romanos[romano[i]] > num_romanos[romano[i - 1]]:
                        dec += conversion(romano[i]) - 2 * conversion(romano[i - 1])
             
        return dec


print(conversion('DXXVII'))

    
        
#22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u
#otro, el que más le guste) está atrapado, pero muy cerca está su mochila que contiene muchos
#objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
#ayuda de la fuerza” realizar las siguientes actividades:
#a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
#queden más objetos en la mochila;
#b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
#car para encontrarlo;
#c. Utilizar un vector para representar la mochila.

mochila = ['mapa', 'botella', 'cuchillo', 'pistola', 'encendedor', 'brujula', 'sable de luz', 'foto de yoda']

def usarLaFuerza(vector, buscado, indice):
        if(indice == len(vector)):
            return -1
        elif(buscado == vector[indice]):
                print ('Elemento encontrado en la posicion : ', indice +1)
                print('Cantidad de items que tuvimos que sacar: ', indice)
                return "buen trabajo!"         
        else:
            return usarLaFuerza(vector, buscado, indice+1)
        


print(usarLaFuerza(mochila, "sable de luz", 0))

#23. Salida del laberinto. Encontrar un camino que permita salir de un laberinto definido en una
#matriz de [n x n], solo se puede mover de a una casilla a la vez –no se puede mover en diagonal–
# que la misma sea adyacente y no esté marcada como pared. Se comenzará en la casilla (0, 0)
#y se termina en la (n-1, n-1). Se mueve a la siguiente casilla si es posible, cuando no se pueda
        #avanzar hay que retroceder sobre los pasos dados en busca de un camino alternativo
