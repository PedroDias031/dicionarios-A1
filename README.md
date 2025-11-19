# dicionarios-A1

🗺️ Consulta Simples de UF (Unidade Federativa)

- Este é um script Python básico que permite ao usuário consultar o nome completo de um estado brasileiro (ou cidade principal) a partir de sua sigla (UF). O programa garante que apenas siglas válidas sejam aceitas antes de exibir o resultado.

✨ Funcionalidades

- Mapeamento UF: Contém um dicionário predefinido que mapeia 10 siglas de Unidades Federativas (UF) aos seus respectivos nomes (ex: SP para São Paulo).

- Validação de Entrada: Utiliza um laço while para solicitar repetidamente a UF ao usuário até que uma sigla válida (presente no dicionário) seja inserida.

- Output Formatado: Exibe o nome do estado/cidade escolhido em letras maiúsculas para clareza.

🛠️ Como Executar

- Este é um script Python puro.

REQUISITOS:

- Python: Versão 3.x
  
EXECUÇÃO:

- Salve o código em um arquivo chamado, por exemplo, consulta_uf.py.

- Abra o IDE ou prompt de comando, navegue até o diretório onde o arquivo está salvo.

➡️ Exemplo de Entrada/Saída (I/O)

- O exemplo demonstra como o script lida com entradas inválidas e exibe o resultado para uma entrada válida.

💡 Estrutura do Código

- O script é dividido em três partes principais:

- Dicionário de Dados (cidades): Define o conjunto de dados (Chave: Sigla, Valor: Nome Completo).

- Lista de Chaves (uf): Cria uma lista das chaves (cidades.keys()) para facilitar a validação da entrada.

- Laço de Validação (while True):

- Solicita a UF e converte a entrada para maiúsculas (.upper()).

- Verifica se a UF digitada está presente na lista uf (validação).

- Se válida, o laço é interrompido (break). Se inválida, exibe uma mensagem de erro e repete a solicitação.

- Impressão do Resultado: Após a validação, usa a UF validada como chave para buscar e imprimir o valor correspondente no dicionário: cidades[city].
