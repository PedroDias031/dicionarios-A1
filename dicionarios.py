cidades = {
    "AC": "Acre",
    "BA": "Bahia",
    "CE": "Ceara",
    "DF": "Distrito Federal",
    "MG": "Minas Gerais",
    "PR": "Paraná",
    "RJ": "Rio de Janeiro",
    "RS": "Rio Grande do Sul",
    "SP": "São Paulo",
    "PE": "Pernambuco"
    }

print('Aqui printa os valores das chaves!')
for city in cidades.values():
    print(city)
    
print('Aqui printa os chaves do dicionario!')
for chave in cidades.keys():
    print(chave)