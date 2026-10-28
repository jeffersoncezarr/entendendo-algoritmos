#Devemos selecionar o valor que ordenaremos naquela rodada...
def menor_item(lista: list)-> int:
    menor_indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[menor_indice]:
            menor_indice = i
    return menor_indice


#Nesse caso usei recursão para remover o menor valor da lista até que ela fique ordenada
#Também podemos usar os loops como alternativa,,,
def selection_sort(lista: list)-> list:
    if len(lista) <= 1:
        return lista
    else:
        return [lista.pop(menor_item(lista))] + selection_sort(lista)


print(selection_sort([1,4,0,22,5,6]))