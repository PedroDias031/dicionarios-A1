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
uf = list(cidades.keys())


while True:
    print('  Informe uma dessas UF para continuar\n AC, BA, CE, DF, MG, PR, RJ, RS, SP, PE.')
    city = input(' UF desejada: ').upper()
    if city in uf: 
        break
    else:
        print('Não foi possivel consultar essa UF tente novamente...')


print (f'A cidade da UF escolhida e: {cidades[city].upper()}')
