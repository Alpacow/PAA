# -*- coding: utf-8 -*-
# Criar um algoritmo, com complexidade O(n log n), que conte o número de inversões de um array.

# MERGE SORT
def mergeSort(v, n):
    aux = [0] * n 
    return mergeSortCount(v, aux, 0, n-1) 

# MERGE SORT QUE CONTA AS INVERSÕES
def mergeSortCount(v, temp, esq, dir): 
    countInv = 0  
    if esq < dir: 
        meio = (esq + dir)//2
        countInv = mergeSortCount(v, temp, esq, meio) 
        countInv += mergeSortCount(v, temp, meio + 1, dir)
        countInv += merge(v, temp, esq, meio, dir) 
    return countInv

def merge(v, temp, esq, meio, dir): 
    i = esq
    j = meio + 1
    k = esq
    countInv = 0
    while i <= meio and j <= dir: 
        if v[i] <= v[j]: 
            temp[k] = v[i] 
            k += 1
            i += 1
        else:
            temp[k] = v[j] 
            countInv += (meio-i + 1) 
            k += 1
            j += 1
    while i <= meio: 
        temp[k] = v[i] 
        k += 1
        i += 1
    while j <= dir: 
        temp[k] = v[j] 
        k += 1
        j += 1
    for loop_var in range(esq, dir + 1): 
        v[loop_var] = temp[loop_var] 
    return countInv 

array = [12, 8, 14, 2, 6, 9, 5]
result = mergeSort(array, len(array))
print("Total de inversoes: %d" %result) 
