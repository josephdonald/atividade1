def selectionSort(tamLista, lista):
    # n = len(lista)
    for j in range(tamLista - 1):
        menor_indice = j

        for i in range(j, tamLista):
            if lista[i] < lista[menor_indice]:
                menor_indice = i
                
        if lista[j] > lista[menor_indice]:
            aux = lista[j]
            lista[j] = lista[menor_indice]
            lista[menor_indice] = aux

    return lista