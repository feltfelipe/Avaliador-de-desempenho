avaliador = {}
time = []
gols = []
while True:
    avaliador.clear()
    gols.clear()
    avaliador['nome'] = str(input('Nome: '))
    avaliador['jogos'] = int(input(f'Quantas partidas {avaliador["nome"]} jogou? '))
    if avaliador['jogos'] == 0:
        break
    else:
        for g in range(avaliador['jogos']):
            gols.append(int(input(f'Quantos gols na {g+1}ª partida? ')))
        avaliador['gols'] = gols[:]
        avaliador['total'] = sum(gols)
        time.append(avaliador.copy())
    while True:
        opção = str(input('Cadastrar outro jogador? [S/N]: ')).upper()[0]
        if opção in 'SN':
            break
        print('Digite S pra sim e N para não.')
    if opção == 'N':
        break
print('-=' * 28)
print(f'{"   >> ANALISADOR DO TIME <<   ":^50}')
print('-=' * 28)
print(f'{"JOGADOR":>10}{"PARTIDAS":>19}{"GOLS":>12}{"TOTAL":>17}')
for k, v in enumerate(time): #para cada posição, no item dentro da lista time:
    print(f'{k:>4}', end=' ') #imprima a posição
    for d in v.values(): #para cada item(v), que é o dicionário adicionado em time
        #analise cada item(d) nos valores do dicionário(v).
        print(f'{str(d):<15}', end=' ') #imprima d(que são os valores), mas imprima tudo como string
    print() #quebra de linha no loop por causa do end acima
print('--' * 35)
while True:
    busca = int(input(f'Digite o cód do jogador para analisar separadamente. [999] para encerrar: '))
    if busca == 999:
        break
    elif busca >= len(time):#atento para não confundir a posição( de 0 a 4) com o tamanho(5). Por isso '>= len()'
        print(f'Jogador {busca} não existe.')
    else:
        print('   >>  ANALISANDO JOGADOR  <<   ')
        print(f'Os dados do jogador {time[busca]["nome"]} são:')
        print('--' * 35)
        for i, g in enumerate(time[busca]['gols']): #Esse enumerate acusa a existencia de uma lista que tem dentro da chave ['gols'] dentro da lista time na
            #posicação 'busca'. Analisando uma lista que está dentro de uma lista dentro do dicionário.
            print(f'=>   No jogo {i+1} fez {g} gols')
        print(f'Aproveitamento de {time[busca]["total"] / time[busca]["jogos"]:.2f} gols por partida.')
        print('--' * 35)
