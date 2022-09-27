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

# Función para identificar cuáles son números primos
#def primos(arr):
#    array2 = []
#    for i in array1:
#        if i%2==1 and i%i==0:
#            array2.append(i)
#    return array2

n=int(sys.argv[1])
array1=arrayCreator(n)
print(array1)
#primos(array1) 