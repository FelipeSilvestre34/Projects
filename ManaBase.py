# Variaveis para as cores de mana
Mana_Base = [] #ira jogar a quantidade de simbolos nas respectivas cores
Mana_Total = [] #Total de Mana considderando somente as cores
Mana_Guild = []
Percent_Mana_Dic = {} #Percental de mana que deve ser considerando para o total de lands
Dual_Land = [] #lands que geram 2 cores, de acordo com a guilda respectiva
Tri_Land = [] #lands que geram 3 cores, de acordo com a guilda respectiva
Four_Land = [] #lands que geram 2 ou 3 cores, de acordo com a guilda respectiva
Full_Land = [] #Todas as Guildas podem ir dentro deste deck
Mana_Color = []
Mana_Guild_Colors = []
Colors_Deck = 0
Guild2 = ''
Lands_Total = 0


print("""

      *****  Calculadora de Base de Mana para Magic: The Gathering  *****

      """)
print('**** Esta calculadora de mana é voltada para decks com mais de 2 cores ****')

############################Dicionario dos tipos de manas################################
Dici_Mana = {'BasicLands': ['Preta', 'Verde', 'Azul', 'Branca', 'Vermelha'],
             'DualLands': {'Azorius': ['Azul', 'Branca'], 'Dimir': ['Azul','Preta'],
                           'Rakdos': ['Preta', 'Vermelha',], 'Gruul': ['Verde', 'Vermelha'],
                           'Selesnya':['Verde', 'Branca'], 'Orzhov': ['Preta', 'Branca'],
                           'Izzet': ['Azul', 'Vermelha'], 'Golgari': ['Preta', 'Verde'],
                           'Boros': ['Branca', 'Vermelha'], 'Simic': ['Verde', 'Azul']},
             'TriLands': {'Esper':['Preta', 'Azul', 'Branca'], 'Grixis':['Preta', 'Azul', 'Vermelha'],
                          'Jund': ['Preta', 'Verde', 'Vermelha'], 'Naya': ['Verde', 'Branca', 'Vermelha'],
                          'Bant': ['Verde', 'Azul', 'Branca'], 'Abzan': ['Preta', 'Verde', 'Branca'],
                          'Sultai':['Preta', 'Verde', 'Azul'], 'Mardu':['Preta', 'Branca', 'Vermelha'],
                          'Temur':['Verde', 'Azul','Vermelha']},
             'FourLands':{'Greenless':['Preta', 'Azul', 'Branca', 'Vermelha'], 'Whiteless':['Preta', 'Verde', 'Azul', 'Vermelha'],
                          'Blueless':['Preta', 'Verde', 'Branca', 'Vermelha'], 'Blackless':['Verde', 'Azul', 'Branca', 'Vermelha'],
                          'Redless': ['Preta', 'Verde', 'Azul', 'Branca']}
}
################################ Funções #############################################
def Guild_Fun(item):
    print('estou aqui')
    Guild2 = ''
    text = 'Azorius Dimir Rakdos Gruul Selesnya Orzhov Izzet Golgari Boros Simic Esper Grixis Jund Naya Bant Abzan Sultai Mardu Temur'
    while True:
        try:
            Guild2 = (input('Qual a guilda do seu deck:  '))
            Guild2 = (Guild2.lower()).capitalize()
        except:
            if text.find(Guild2) == -1:
                print('Favor inserir sua guilda')
        else:
            break
    return Guild2

#Etapa 1 -> Verifica a guilda do deck e condiciona a Mana_Base e Mana_Color
def Multi_color(Colors_Deck_Arg1,guild_args):
    if Colors_Deck == 2:
        Dual_Land = Dici_Mana['DualLands'][Guild]
        return Dual_Land
    if Colors_Deck == 3:
        Dual_Land = Dici_Mana['DualLands']
        Tri_Land = Dici_Mana['TriLands'][Guild]
        return Tri_Land
    if Colors_Deck == 4:
        Four_Land = Dici_Mana['FourLands'][Guild]
        return Four_Land
    else:
        Full_Land = Dici_Mana['BasicLands']
        return Full_Land

#Etapa 2 -> Função que ira registrar a quantidade de cada tipo de mana
def Mana_Base_Def(Colors_Deck_Arg2,Mana_Color_Arg):
    i = 0
    Mana_Def = Mana_Color
    if Colors_Deck == 2:
        for k in range(len(Mana_Def)):
            Mana_Base.append(Mana_Def[k])
        return Mana_Color, Mana_Base
    if Colors_Deck ==3:
        for k in range(len(Mana_Def)):
            Mana_Base.append(Mana_Def[k])
        return Mana_Def, Mana_Color
    if Colors_Deck ==4:
        for k in range(len(Mana_Def)):
            Mana_Base.append(Mana_Def[k])
        return Mana_Def, Mana_Color
    else:
        for k in range(len(Mana_Def)):
            Mana_Base.append(Mana_Def[k])
        return Mana_Def, Mana_Color

#Etapa 3 -> ira ver a quantida de mana de cada cor
def Mana_Base_Colors(Mana_Base_def,Mana_color_def):
    i = 0
    Mana = 0
    Mana_Guild_Colors = Mana_Base
    for valor in Mana_Base:
        Mana_Guild_Colors[i] = int(input(f'Quantos Símbolos de mana {Mana_Base[i]} tem no seu deck:  '))
        text = (f'Cor(es) de mana(s) {Mana_Color[i]}: {Mana_Guild_Colors[i]}')
        Mana_Total.append(text)
        i += 1
    Mana_Total.append(f'O Total de cor(es) de mana(s): {sum(Mana_Guild_Colors)}')
    return Mana_Guild_Colors

#Etapa 4 retorno os valores de cada tipo de mana para o usuário
def Calculate_Mana(Guilda_Cal,Mana_Guild_Cal):
    ManaRes = 0
    i = 0
    Total = sum(Mana_Base)
    print(Total)
    if Colors_Deck == 2:
        Mana_Guild = Dici_Mana['DualLands'][Guild]
    elif Colors_Deck == 3:
        Mana_Guild = Dici_Mana['TriLands'][Guild]
    elif Colors_Deck == 4:
        Mana_Guild = Dici_Mana['FourLands'][Guild]
    else:
        Mana_Guild = Dici_Mana['BasicLands']
    for value in Mana_Base:
        Percent_Mana = Mana_Base[i]/Total
        ManaRes += Mana_Base[i] - Percent_Mana
        Valor = round(Percent_Mana * Lands_Total)
        Percent_Mana_Dic[Mana_Color[i]] = Valor

        i += 1

    print(Mana_Total)
    print(Percent_Mana_Dic)
    return Percent_Mana_Dic




################################ INÍCIO DO CÓDIGO #####################################
######################## Definindo Quantide de Mana ####################################
while True:
    try:
        Lands_Total = int(input('Qual o total de Mana(s) que vai colocar no deck:  ')) #total de lands que vai no deck
    except ValueError:
        print('Favor inserir quantidade de mana que ira no deck!')
    else:
        break

######################## Definindo as cores do deck ####################################
print('A quantidade de cor vai de 1 até 5 cores')
while True:
    try:
        Colors_Deck = int(input('Quantas cores tem o seu deck:  ')) #Quantidade de cores que e o Deck tem
    except ValueError:
        print('A quantidade de cor vai de 1 até 5 cores')
    else:
        break

############### VERIFICAÇÃO DA QUANTIDADE DE CORES DO DECK PARA INICIAR A DISTRUIBUIÇÃO DAS MANAS
if Colors_Deck == 1:
    print(f'O total de mana que você precisa é igual a: {Lands_Total}  mana(s)')
elif Colors_Deck ==2:
    print('Guildas: Azorius, Dimir, Rakdos, Gruul, Selesnya, Orzhov, Izzet, Golgari, Boros, Simic')
    Guild_Fun(Colors_Deck)
    Guild = Guild_Fun(Guild2)
    Multi_color(Colors_Deck,Guild) # Etapa 1
    Mana_Color = Multi_color(Dual_Land)
    Mana_Base_Def(Colors_Deck,Mana_Color) # Etapa 2
    Mana_Base_Colors(Mana_Color, Mana_Base) # Etapa 3
    Calculate_Mana(Mana_Color, Mana_Base) # Etapa 4
elif Colors_Deck ==3:
    print('Guildas: Esper, Grixis, Jund, Naya, Bant, Abzan, Sultai, Mardu, Temur')
    while Guild == '':
        Guild = (input('Qual a guilda do seu deck:  ')).capitalize()
    Multi_color(Colors_Deck,Guild) # Etapa 1
    Mana_Color = Multi_color(Tri_Land)
    Mana_Base_Def(Colors_Deck,Mana_Color) # Etapa 2
    Mana_Base_Colors(Mana_Color, Mana_Base) # Etapa 3
    Calculate_Mana(Mana_Color, Mana_Base) # Etapa 4
elif Colors_Deck ==4:
    print('Comandantes 4 cores: Breya, Yidris, Omnath, Atraxa')
    print('Guildas: Glint, Dune, Ink, Witch, Yore')
    print('Qual a cor que não tem no seu deck: Greenless, Whiteless, Blueless, Blackless, Redless')
    while Guild == '':
        Guild = (input('Qual a cor que não tem no seu deck:  ')).capitalize()
    Multi_color(Colors_Deck) # Etapa 1
    Mana_Color = Multi_color(Four_Land)
    Mana_Base_Def(Colors_Deck,Mana_Color) # Etapa 2
    Mana_Base_Colors(Mana_Color, Mana_Base) # Etapa 3
    Calculate_Mana(Mana_Color, Mana_Base) # Etapa 4
else:
    Guild = '5 Cores'
    Multi_color(Colors_Deck) # Etapa 1
    Mana_Color = Multi_color(Full_Land)
    Mana_Base_Def(Colors_Deck,Mana_Color) # Etapa 2
    Mana_Base_Colors(Mana_Color, Mana_Base) # Etapa 3
    Calculate_Mana(Mana_Color, Mana_Base) # Etapa 4
##################################### FIM DO CÓDIGO ###################################



input("""

      Pressione Enter para sair

      """)
# Black, Green, Blue, White, Red = tuple(ManaBase) joga os valores da lista em cada cor de mana
