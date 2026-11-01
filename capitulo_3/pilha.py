#No livro é falado sobre pilha usando o exemplo de chamada de recursão, onde quando a recursão chega ao caso base
#Ela vai retornando seus valores da ultima chamada para a primeira.
#Nesse caso utilizo um exemplo aprendido em outro livro, usando uma pilha de pratos, onde seguimos a mesma logica.
#Aqyi assim como uma pilha de pratos a serem lavados, adicionamos o item ao final e esse ultimo item adicionado
#Será o primeiro a ser lavado...

class PilhaPratos:
    def __init__(self):
        self._pilha = []
        self._ultimo = 1


    def __str__(self):
        return f'PILHA DE PRATOS: {self.pilha}  QUANTIDADE DE PRATOS A LAVAR: {len(self)}'


    def __len__(self):
        return len(self.pilha)


    @property
    def ultimo(self):
        return self._ultimo


    @property
    def pilha(self):
        return self.pilha


    def adicionar_prato(self):
        self._pilha.append(self._ultimo)
        self._ultimo += 1
        print('Prato adicionado a pilha')


    def lavar_prato(self):
        if self.pilha:
            self.pilha.pop(-1)
        print('Não há pratos para lavar!')


    def proximo_prato(self):
        if self.pilha:
            return f'PROXIMO PRATO A LAVAR: {self.ultimo}'
        return 'A PILHA DE PRATOS ESTÁ VAZIA!'

