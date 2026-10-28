#Para criarmos uma lista encadeada é necessario criar um novo tipo de dado
#Que armazenará um valor e o endereço do proximo elemento da lista, chamaremos de No.

class No(object):
    def __init__(self, valor):
        self.valor = 