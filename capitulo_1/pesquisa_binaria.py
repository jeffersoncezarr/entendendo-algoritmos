"""

A pesquisa binária nos permite otimizar o tempo de busca numa lista ordenada.

Utilizando dois extremos, neste caso utilizaremos duas variáveis (alto e baixo) e um chute (no índice que corresponde à
metade da soma de alto e baixo).

Tempo de execução -> O(log n)

"""

numb_list = [1,8,6,20,2,65,23,100]
# Lembrando que na pesquisa binaria é obrigatorio que os itens estejam ordenados...
# Neste caso usarei uma função integrada, mas poderiamos por exemplousar a ordenação por seleção que veremos a frente...
numb_list.sort()

def binary_search(items_list, select_item):
    high = len(items_list) - 1
    low = 0

    while high >= low:
        middle = (high + low)//2
        attemp = items_list[middle]

        if attemp ==  select_item: # Se nosso chute for certo, ele retornará a mensagem
            return f'Número {select_item} encontrado na posição: {middle}'
        elif attemp > select_item: # Caso a tentativa for maior que o numero sorteado , alteramos o high value
            high = middle - 1
        else: # Em caso do chute menor, atualizamos o low value
            low = middle + 1

    return 'Numero não está na lista!'


if __name__ == '__main__':
    print(binary_search(numb_list, 20))