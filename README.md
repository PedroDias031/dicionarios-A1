# dicionarios-A1

🗺️ Consulta Simples de UF (Unidade Federativa)

- Este é um script Python básico que permite ao usuário consultar o nome completo de um estado brasileiro (ou cidade principal) a partir de sua sigla (UF). O programa garante que apenas siglas válidas sejam aceitas antes de exibir o resultado.

✨ Funcionalidades

- Mapeamento UF: Contém um dicionário predefinido que mapeia 10 siglas de Unidades Federativas (UF) aos seus respectivos nomes (ex: SP para São Paulo).

- Validação de Entrada: Utiliza um laço while para solicitar repetidamente a UF ao usuário até que uma sigla válida (presente no dicionário) seja inserida.

- Output Formatado: Exibe o nome do estado/cidade escolhido em letras maiúsculas para clareza.

📝 Estrutura do Algoritmo
Abaixo está o pseudocódigo que representa a lógica do script. O pseudocódigo é uma ferramenta fundamental na representação de algoritmos, pois permite descrever o fluxo lógico antes da codificação em uma linguagem específica.

ALGORITMO Mapeamento UF

VARIAVEIS

    cidades : DICIONÁRIO // Mapeia UF (chave) para Nome do Estado (valor)
    
    uf : LISTA          // Contém apenas as chaves (UFs) do dicionário cidades
    
    city : STRING       // Armazena a UF digitada pelo usuário
INÍCIO

    // 1. Definição da Estrutura de Dados
    cidades = {
        "AC": "Acre",
        "BA": "Bahia",
        ...
        "PE": "Pernambuco"
    }
    uf = extrair_chaves_do_dicionario(cidades)
    
    // 2. Estrutura de Repetição (Loop) para Validação de Entrada
    REPITA
        // 2.1. Solicitar Entrada ao Usuário
        IMPRIMA "Informe uma dessas UF para continuar: AC, BA, CE, DF, MG, PR, RJ, RS, SP, PE."
        LEIA city
        city = converter_para_maiusculas(city)
        
        // 2.2. Estrutura Condicional para Checagem
        SE city PERTENCE_A uf ENTÃO
            PARE O LAÇO DE REPETIÇÃO
        SENÃO
            IMPRIMA "Não foi possível consultar essa UF, tente novamente..."
        FIM_SE
    ENQUANTO VERDADEIRO
    
    // 3. Apresentação do Resultado
    nome_da_cidade = valor_do_dicionario(cidades, city)
    nome_da_cidade = converter_para_maiusculas(nome_da_cidade)
    IMPRIMA "A cidade da UF escolhida é: " + nome_da_cidade
FIM

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
