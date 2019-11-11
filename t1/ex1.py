# -*- coding: utf-8 -*-
# Ex 1: algoritmo n.log(n) que verifica se 2 valores em um array é = x.

# QUICK SORT -> O(n log n)
def particao(v , menor, maior):
    i = (menor - 1)
    pivo = v[maior]
    for j in range(menor, maior):
        if v[j] <= pivo:
            i += 1 #incrementa indice do menor elemento
            v[i], v[j] = v[j], v[i] # realiza trocas
    v[i+1], v[maior] = v[maior], v[i+1]
    return i + 1

def quickSort(v, menor, maior):
    if menor < maior:
        idx = particao(v, menor, maior)
        quickSort(v, menor, idx - 1)
        quickSort(v, idx + 1, maior)

# ENCONTRAR SOMA PARES = X -> O(n)
def mostraSoma(v, x, n):
    i = 0
    j = n - 1;
    while(i < j):
        if(v[i] + v[j] == x):
            print("(%d, %d)\n" %(v[i], v[j]))
            i += 1
            j -+ 1
        elif(v[i] + v[j] > x):
            j -= 1
        else:
            i += 1

array = [12, 8, 14, 2, 6, 9, 5]
n = len(array) - 1
x = 14
quickSort(array, 0, n)
mostraSoma(array, x, n)

#O(n log n) + O(n) = O(n log n + n) = O(n log n), n < n log n quando n é mt grande
