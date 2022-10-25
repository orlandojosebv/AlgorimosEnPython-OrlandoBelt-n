
#Algoritmo de Búsqueda Binaria
#Código extraído de https://programacionpython80889555.wordpress.com/2021/12/22/algoritmos-en-python-busqueda-binaria/#:~:text=Tambi%C3%A9n%20llamada%20%C2%ABb%C3%BAsqueda%20de%20intervalo,modo%20que%20si%20ambos%20no
from operator import truediv
from re import L


def busquedaBinaria(lista,valor):
    steps = 0
    izq=0
    der=len(lista)-1
    while izq<=der:
        steps=+1
        puntoMedio=(izq+der)/2
        if lista[puntoMedio]==valor:
            return "Valor encontrado en {} pasos, en la posición {}.".format(steps,puntoMedio)
        if lista[puntoMedio]>valor:
            der= puntoMedio-1
        if lista[puntoMedio]<valor:
            izq=puntoMedio+1
    return "Elemento no encontrado."



#Algoritmo de Búsqueda lineal
#Código extraído de https://programacionpython80889555.wordpress.com/2021/12/22/algoritmos-en-python-busqueda-binaria/#:~:text=Tambi%C3%A9n%20llamada%20%C2%ABb%C3%BAsqueda%20de%20intervalo,modo%20que%20si%20ambos%20no

def busquedaLineal(lista, valor):
    steps=0
    for i, item in enumerate(lista):
        steps+=1
        if item==valor:
            return "Valor encontrado en {} pasos en la posicion {}.".format(steps,i)
    return "Elemeno no encontrado."


#Algoritmo de ordenamiento #1- Bubble sort
#Código extraído de https://www.geeksforgeeks.org/python-program-for-bubble-sort/

def bubbleSort(arr):
    n = len(arr)

    swapped=False
    for i in range(n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped=True
                arr[j],arr[j+1],arr[j]
        if not swapped:
            return


#Algoritmo de ordenamiento #2-Merge Sort
#Codigo extraído de https://www.geeksforgeeks.org/merge-sort/  by Mayank Khanna
def mergeSort(arr):
    if len(arr) > 1:
 
         # Se encuentra la mitad del array
        mid = len(arr)//2
 
        # Se Divide el array para el lado izquierdo
        L = arr[:mid]
 
        #Se divide el array para el lado derecho
        R = arr[mid:]
 
        # Se ordena la primera mitad del array
        mergeSort(L)
 
        # Se ordena la segunda mitad del array
        mergeSort(R)
 
        i = j = k = 0
 
        # Se crean sub- arrays del array original
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Verificamos si queda algun elemento del array restante
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

#Algoritmo  de ordenamiento #3-Insertion Sort
#Algoritmo tomado de https://www.geeksforgeeks.org/insertion-sort/  By Mohit Kumra

def insertionSort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key < arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


#Algoritmo para imprimir un array 
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
           



if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array is: ", end="\n")
    printList(arr)
    mergeSort(arr)
    print()
    print("Sorted array is: ", end="\n")
    printList(arr)       