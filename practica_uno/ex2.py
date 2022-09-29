# Ejercicio 2 Luis Alberto Carranza González A01657296
# Librerías
import sys

# Función para crear arreglos desde 1 hasta n
def arrayCreator(n):
   array1 = []
   i=1
   for i in range(i,n+1):
      array1.append(i)
   return array1

# Función para crear array de números primos
def arrayCreator2(array1):
    array2=[]
    for i in range(2,n+1):
        num=primo(i)
        if num==True:
            array2.append(i)
    return array2

# Función para identificar números primos
def primo(i):
    for n in range(2,i):
        if i % n == 0:
            return False
    return True

# Input
n=int(sys.argv[1])

# Llamar a funciones
array1=arrayCreator(n)
array2=arrayCreator2(array1)

# Imprimir arreglos
print(array1)
print(array2) 