#Para criarmos uma lista encadeada é necessario criar um novo tipo de dado
#Que armazenará um valor e o endereço do proximo elemento da lista, chamaremos de No.

class No(object):
    def __init__(self, valor)-> None:
        self.valor = valor
        self.proximo = None


class ListaEncadeada(object):
    def __init__(self)-> None:
        self.atual = None


    def adiciona_item(self, valor)-> None:
        if self.atual:
            ponteiro = self.atual
            while ponteiro.proximo:
                ponteiro = ponteiro.proximo
            ponteiro.proximo = No(valor)
        else:
            self.atual = No(valor)

    def mostrar_lista(self):
        ponteiro = self.atual
        while self.atual:
            print(ponteiro.valor, end=' ')
            self.atual = ponteiro.proximo
            ponteiro = self.atual


l1 = ListaEncadeada()
l1.adiciona_item(2)
l1.adiciona_item(3)
l1.mostrar_lista()
