# dicionarios-A1

🗺️ Explorando Dicionários em Python
Este projeto simples demonstra o uso e a iteração sobre dicionários em Python, uma estrutura de dados fundamental para armazenar pares de chave-valor (key-value pairs). O exemplo foca em como acessar e exibir separadamente as chaves (abreviações de estados) e os valores (nomes dos estados).

⚙️ Como Funciona
O código é dividido em três partes principais: a criação do dicionário e duas iterações diferentes sobre seus elementos.

1. Criação do Dicionário (cidades)
O dicionário cidades mapeia as abreviações dos estados brasileiros (chaves) para os nomes completos dos estados (valores).

2. Iteração pelos Valores (.values())
Esta seção utiliza o método .values() para retornar uma "visão" dos valores do dicionário.

3. Iteração pelas Chaves (.keys())
Esta seção utiliza o método .keys() para retornar uma "visão" das chaves do dicionário.
O laço for itera sobre todas as chaves do dicionário.

Saída: Exibe apenas as abreviações dos estados, como "AC", "BA", "CE", etc.

💻 Execução
Pré-requisitos:
Python 3 instalado.

Execução:
Salve o código em um arquivo chamado, por exemplo, dicionario_estados.py.

Execute o script no terminal:

Bash

python dicionario_estados.py
Resultado Esperado:
Aqui printa os valores das chaves!
Acre
Bahia
Ceara
Distrito Federal
Minas Gerais
Paraná
Rio de Janeiro
Rio Grande do Sul
São Paulo
Pernambuco
Aqui printa os chaves do dicionario!
AC
BA
CE
DF
MG
PR
RJ
RS
SP
PE
💡 Conceito Chave: Dicionário
Um dicionário é uma coleção não ordenada (no Python moderno, é inserção ordenada) de itens. Cada item consiste em uma chave e um valor.

Chave (Key): Deve ser única e imutável (como strings, números ou tuplas). Serve como o índice para encontrar o valor.

Valor (Value): Pode ser qualquer tipo de dado (string, número, lista, outro dicionário, etc.).
