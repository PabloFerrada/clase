import numpy as np


numero= np.random.randint(0,11 , size=100)
print(numero)
for i in (numero%2==0):
    print (i)

print(numero.max())
mayor= numero.max()


# Representa al contador para el ciclo While True
indice = 0

def indiceMayor():

    while True:
        # Si el elemento en el indice actual es igual al numero mayor entonces lo devuelve
        if (numero[indice] == mayor):
            return numero[indice]
        
        # Si no es igual, entonces da otra vuelta al ciclo y se aumenta el indice en 1
        else:
            indice + 1

print(indiceMayor())