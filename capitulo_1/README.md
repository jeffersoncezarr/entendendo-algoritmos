Pesquisa Binária: 

Um algoritmo de pesquisa binária nos permite otimizar o tempo de busca em uma lista em tempo O(n), ou seja, performa em tempo logarítmico. No entanto, é obrigatório que a lista esteja ordenada. A pesquisa binária consiste em utilizarmos o índice mediano para nos localizarmos e conseguirmos encontrar o número desejado. Ou seja, em uma lista de 100 itens ordenados, temos dois polos (alto e baixo) que nos auxiliam a encontrar o índice mediano, somando as duas extremidades e fazendo uma divisão inteira do resultado; desta forma, temos o índice de chute.

Caso o índice mediano esteja abaixo do valor desejado, a extremidade "baixo" será atualizada com o valor do índice mediano + 1, já que temos certeza de que o índice mediano não corresponde ao valor desejado.

Em caso de o índice mediano ser mais alto do que o valor desejado, será necessário atualizar a extremidade "alto" para o valor do índice mediano – 1, já que nesse caso temos certeza de que o valor atual do índice mediano não corresponde ao valor desejado.

Em contrapartida à pesquisa binária, podemos utilizar a pesquisa simples, que atua em tempo linear, ou seja, cresce na mesma proporção que a lista, visto que, na pesquisa simples, é validado item por item. Nesse caso, enquanto em uma lista de 100 itens a pesquisa binária no pior dos casos executa no máximo 7 etapas, a pesquisa simples executa até 100.

É importante lembrar que o tempo de execução dos algoritmos não cresce de forma proporcional de um para o outro.

Notação Big O:

A notação Big O nos permite comparar a proporção em que o tempo de execução de um algoritmo cresce.
Em notação Big O, a pesquisa simples é O(n), já a pesquisa binária é O(n).

- Pesquisa simples: O(n) -> Tempo de execução linear
- Pesquisa binária: O(n) -> Tempo de execução logarítmico
- 
É importante lembrar que a Notação Big O calcula sempre o tempo de execução na pior das hipóteses, ou seja, mesmo que em uma execução o tempo seja menor, o tempo de execução considerado ainda será o da pior hipótese.

Foram apresentados também alguns dos tempos de execução mais comuns:

O(log n) -> O(n) -> O(n * log n) -> O(n*n) -> O(n!)
