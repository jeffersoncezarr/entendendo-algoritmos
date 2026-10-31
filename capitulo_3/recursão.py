#A recursão nos permite executar tarefas que poderiam ser resolvidas com loops de forma mais elegante
#Na maioria dos casos quando usamos recursao dentro de uma lista , o nosso caso base será ela vazia ou com 1 elemento
#Nesse caso como precisamos somar os elementos da lista, nosso caso base será ela vazia
#Quando o tamanho da lista for 0, esse será o nosso primeiro retorno da pilha de chamadas.

def soma_elementos(lista: list)-> int|float:
    if len(lista) < 1:
        return 0
    else:
        return lista.pop() + soma_elementos(lista)

#Nesse caso invertemos uma string, usando o slice de string como apoio
#O caso base novamente, nesse caso é quando a lista estiver vazia

def invert_string(palavra: str)-> str:
    if len(palavra) == 0:
        return ''
    else:
        return palavra[-1] + invert_string(palavra[:len(palavra)-1])
