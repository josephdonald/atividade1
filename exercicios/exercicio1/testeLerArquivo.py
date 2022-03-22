import insertion, selection

def lerArquivoInsertion(arquivo):

    with open(arquivo) as arquivoAberto:
        listaNumeros = []
        for linha in arquivoAberto:
            listaNumeros.append(int(linha))
        tamanho = listaNumeros.pop(0)
        print("INSERTION - Lista Original:", listaNumeros)
        listaOrdenada = insertion.insertSort(tamanho, listaNumeros)
        print("INSERTION - Lista Ordenada:", listaOrdenada)


lerArquivoInsertion("num.1000.1.in")


def lerArquivoSelection(arquivo):
    with open(arquivo) as arquivoAberto:
        listaNumeros = []
        # listaOrdenada = []
        for linha in arquivoAberto:
            listaNumeros.append(int(linha))
        tamanho = listaNumeros.pop(0)
        print("#############")
        # print("Tamanho da lista:", tamanho)
        print("SELECTION - Lista Original:", listaNumeros)
        listaOrdenada = selection.selectionSort(tamanho, listaNumeros)
        print("SELECTION - Lista Ordenada:", listaOrdenada)


lerArquivoSelection("num.1000.1.in")