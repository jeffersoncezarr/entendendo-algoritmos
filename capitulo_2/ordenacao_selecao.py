#Devemos selecionar o valor que ordenaremos naquela rodada...
def lowest_value(lista: list)-> int:
    item_index = 0
    for i in range(len(lista)):
        if lista[i] < lista[item_index]:
            item_index= i
    return item_index


#Nesse caso usei recursão para remover o menor valor da lista até que ela fique ordenada
#Também podemos usar os loops como alternativa,,,
def selection_sort(lista: list)-> list:
    if len(lista) <= 1:
        return lista
    else:
        return [lista.pop(lowest_value(lista))] + selection_sort(lista)


print(selection_sort([1,4,0,22,5,6]))