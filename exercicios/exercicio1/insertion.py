def insertSort(tamLista, listaNumeros):

    for i in range(1, tamLista):
        chave = listaNumeros[i]
        j = i - 1
        while (j >= 0 and listaNumeros[j] > chave):
            listaNumeros[j + 1] = listaNumeros[j]
            j = j - 1
            listaNumeros[j + 1] = chave
            # print("Indice atual:", i)

    return listaNumeros