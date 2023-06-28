import numpy as np 
# Actividad 2
# 1.1 Crear un arreglo unidimensional de tamaño 10, con elementos aleatorios de números enteros del 0 al 100, 
# para ello deberá investigar la función que permita crear números aleatorios.

# 1.2. Crear una copia del arreglo y muestre:
# Elemento mayor
# Elemento menor
# Suma de los elementos
# Promedio de los elementos
# Mostrar todos los elementos


# import random 
# numero= np.arange (10)
# print(random.randrange(0,101))
# vector= []

# for numeros in range (10):
#     numeros=random.randint (0,100)
#     vector.append (numeros)
# print (vector)


# arreglo = np.random.randint(0, 100, size=10)
# print(arreglo)

# arreglo1= arreglo.copy()
# print (arreglo1.min())
# print (arreglo1.max())
# print(arreglo1.sum())
# print(arreglo.mean())
# print(arreglo1)

#-------------------------------------
# Tamaño de la lista.
# Copiar una lista.
# Borrar los elementos de la lista.
# Contar un elemento x de la lista


# animales=["donga","gnomillo","luffy"]
# #copiar
# animales2=animales
# print(animales2)
# #el largo de la lista
# print(len(animales))
# print (animales[0])
# print(len(animales[0]))


 
# animales.remove("donga")
# animales.clear()
# import numpy as np

# lista = [[1,2,3],[4,5,6]]

# matriz= np.array([[1,2,3],[4,5,6]])
# print (matriz [1,1])
# print (matriz[:,2])
# print(matriz[0,:])
# print (matriz[0,::-1])

#________________--------------------------------------------
# Crear un arreglo de dos dimensiones de tamaño 3 x 3, 
# con elementos aleatorios de números enteros del 0 al 100.

# Utilice las siguientes funciones en el arreglo creado en el punto 1
# Promedio de los elementos.
# Suma de los elementos.
# Mostrar el elemento mayor.
# Mostrar el elemento menor.
# Mostrar sólo los elementos de la diagonal principal.

# Crear un arreglo de dos dimensiones de 3 x 3 con números ceros, excepto la
# diagonal principal que debe contener en el mismo orden los siguientes elementos 1, 2 y 3.

# monos= np.random.randint(0,100, size=[3,3])
# print (monos)
# print (monos.mean())
# print(monos.sum())
# print(monos.min())
# print(monos.max())
# print(monos.diagonal())

# numeros= np.zeros (9).reshape(3,3)
# numeros=np.diag([1,2,3])


# print (numeros)


# def salude():
#     print ("hola pete")


# salude()


# def suma(a,b):
#     suma = a+b
#     return (suma)

# num1=int(input("ingresa un numero"))
# num2=int(input("ingresa un numero"))
# print (f"el resultado es:{suma(num1,num2)}" )

#--------------------------------------------------------------


# Se pide escribir las instrucciones necesarias para crear un menú con las opciones de:
# Calcular_Iva
# Descuento
# Calcular_Imc

# Las cuales deben ser desarrolladas en funciones (métodos).

# Donde:
# Calcular_Iva: Es el precio del producto, multiplicado por el 19% (0.19)
# descuento: Es el precio del producto menos el descuento por aplicar. Mostrar el valor final del producto.
# Calcular_Imc: Índice de masa corporal. Su fórmula es:

# además se debe mostrar el estado de la persona de acuerdo a la siguiente tabla:








# precio=int(input("ingrese un monto: $"))
# def  calcular_iva(precio):
#     preciodeliva=precio*0.19

#     return preciodeliva     #debe señalar que retornar 


# print (calcular_iva(precio))


# valorProducto=int(input("ingrese monto"))
# def calcular_descuento(valorProducto):
#     preciodescuento=valorProducto*0.20
#     preciofinal= valorProducto-preciodescuento
#     return preciofinal


# print (calcular_descuento(valorProducto))

peso=int(input("ingrese su peso:"))
altura=float(input("ingrese su altura:"))


def Calcular_imc(peso,altura):
   alturax2= altura*altura
   imce=peso/alturax2
   if (imce >=18.5):
       print("le faltan cazuelas amike")

   elif (imce >=18.6 and imce<= 24.9):
       print("tas bieen")
   elif (imce >=25.0 and imce <= 29.9):
       print("tas waton")
   elif(imce >=30.0 and imce<=34.9):
       print("muy waton")
   elif (imce >=35.0 and imce <=39.9):
       print ("uf viejito bajale al bajon")
   elif(imce <= 40.0):
       print("rueda de aki prro")
   





    


    