import random
import numpy as np
# 1).- Se requiere crear un vector de tamaño 100, completar los valores del vector aleatoriamente con
# números enteros del 0 al 10, para ello deberá investigar la función que permita crear números
# aleatorios.
vector=[]
for numeros in range (101):
    numeros=random.randint (0,10)
    vector.append (numeros)

print (vector)
# 2).- Mostrar por pantalla sólo los valores que se encuentren en los índices pares
indicesPares=vector [2:100:2]
print (f"los valores pares son {indicesPares}")

# 3).- Mostrar el elemento mayor, sólo 1 en caso de repetirse.
print ("elvalormayor es ", max(vector))


# 4).- Mostrar el índice (posición) del elemento mayor.
for indice, elemento in enumerate (vector):
    #Si el elemento es igual al numero mayor (que en este caso es 10) entonces imprime el indice del elemento
    if elemento ==max(vector):
        print ("el indice del elemento mayor es ",indice)
        break

# 5).- Mostrar el elemento menor.

print("el valor menor es",min(vector))

# 6).- Mostrar el índice del elemento menor.
for indice, elemento in  enumerate (vector):
    if elemento== min (vector):
        print( "el indice del elemento menor es :",indice )
        break



# 7).- Crear un Vector de tamaño 10 que almacene nombres de personas.

# nombre= np.arange (10)
# print (nombre)
lista_nombres=[]

for i in range (10):
    lista_nombres.append ("")
print (lista_nombres)


# 8).- Crear un menú con las opciones: 1) Agregar persona


# 2)Ver Persona
# Donde agregar permita ingresar el nombre de una persona por pantalla mientras el vector no esté
# completo.
# Ver persona permite ver el nombre del índice ingresado por pantalla
#guardar un incide y buscarlo



contador = 0
largo_de_la_lista = len(lista_nombres)

# Mientras la ultima posicion este vacia, permite agregar nombres
while lista_nombres[-1] == "":
    
    opciones= input("escoge una opcion 1). Agregar Persona  2). Ver persona\n")

    if opciones =="1":
        
        nombre_input= input("ingrese su nombre jovencillo \n")
        
        lista_nombres[contador] = nombre_input
        contador += + 1

    elif opciones=="2":
        indice_input= int(input("ingrese el indice jovencillo \n"))

        # Si el indice ingresado essta fuera de rango
        if(indice_input > largo_de_la_lista):
            print("Indice fuera de rango, el rango maximo es ", largo_de_la_lista)
        
        elif(lista_nombres[indice_input] == ""):
            print("No hay ni un weon/a")
        
        # Finalmente si ingresaste un indice valido va a imprimir el nombre
        else:
            print(lista_nombres[indice_input])   



