'''/****************************************************************************
Autor: LUAN RODRIGUES ARAÚJO
Componente Curricular: EXA 854 - MI - Algoritmos
Concluído em: 05/05/2023
Declaro que este código foi elaborado por mim de forma 
individual e não contém nenhum trecho de código de outro colega 
ou de outro autor, tais como provindos de livros e apostilas, e 
páginas ou documentos eletrônicos da Internet. Qualquer trecho 
de código de outra autoria que não a minha está destacado com 
uma citação para o autor e a fonte do código, e estou ciente que 
estes trechos não serão considerados para fins de avaliação.
*****************************************************************************'''
#Python 3.10

#Importar biblioteca random
import random

#gerar numero aleatorio, num1 e num2 recebe o primeiro numero e o ultimo que deverá gerar o numero
def aleatorio(num1,num2):
    return random.randint(num1,num2)

#funcao para mostrar tabuleiro
def tabuleiro(matriz, cor):
    numero = 0
    print('  0 1 2 3 4 5 6 7 8 9')
    for linha in matriz:
        print(str(numero)  + ' ' + cor + ' '.join(linha) + '\033[m')
        numero += 1
    print('=-' * 26 + '\n')

#funcao para gerar matriz
def cria_matriz():
    matriz = []
    for x in range(10):
        linha = []
        matriz.append(linha)
        for y in range(10):
            linha.append('~')
    return matriz

#criacao dos tabuleiros
inimigo = cria_matriz()
voce = cria_matriz()
computador = cria_matriz()

#Funcao para ler e tratar numero inteiro
def ler_int(var1, var2):
    while True:
        try:
            var1 = int(input('Posicione o barco na coordenada '+ var2 + '\n'))
            return var1
        except ValueError:
            print('\nDados inseridos incorretamente, tente novamente:')

#Funcao para escolher e tratar posicao horizontal e vertical
def orientacao():
    orientacao = input('h para horizontal, v para vertical\n')
    while orientacao != 'h' and orientacao != 'v':
        orientacao = input('Você deve usar h para horizontal, v para vertical\n')
    return orientacao

#funcao para posicionar os barcos do usuário, vezes = quantas vezes o barco será gerado, qtd = quantidade de barcos, limite = não ultrapassar tabuleiro
def posicionar(vezes, qtd, limite):
    a = int()
    for n in range(vezes):
        print('NA ORDEM: 3 BARCOS "BB", 2 BARCOS "BBB", 1 BARCO "BBBB"')
        x = ler_int(a,'x ⇾')
        y = ler_int(a,'y ↓')

        orient = orientacao()
        
        if orient == 'h':
            while y > limite or y < 0 or x < 0 or x > 9:
                print('\nVocê não pode ultrapassar o tabuleiro, tente novamente:')
                x = ler_int(a,'x ⇾')
                y = ler_int(a,'y ↓')
                
                orient = orientacao()

            for n in range(qtd):
                while voce[x][y+n]=='B' or voce[x][y] == 'B':
                    print('\nVocê não pode posicionar um dos barcos onde já existe outro, tente novamente:')
                    x = ler_int(a,'x ⇾')
                    y = ler_int(a,'y ↓')
                    orient = orientacao()
            for i in range(qtd):
                voce[x][y+i]='B'

        else:
            while x > limite or y < 0 or x < 0 or y > 9:
                print('\nVocê não pode ultrapassar o tabuleiro, tente novamente:')
                x = ler_int(a,'x ⇾')
                y = ler_int(a,'y ↓')
                orient = orientacao()
            for n in range(qtd):    
                while voce[x+n][y]=='B' or voce[x][y]=='B':
                        print('\nVocê não pode posicionar um dos barcos onde já existe outro, tente novamente:')
                        x = ler_int(a,'x ⇾')
                        y = ler_int(a,'y ↓')
                        orient = orientacao()
            for i in range(qtd):
                voce[x+i][y]='B'
        
        tabuleiro(voce, '\033[5;37;44m')    

#posiciona barcos do usuário
def barcos():
      posicionar(3, 2, 8)
      posicionar(2, 3, 7)
      posicionar(1, 4, 6)

#Tiro inimigo
def tiro_inimigo():
    global pc_ponto
    placar()
    dano1 = aleatorio(0,9)
    dano2 = aleatorio(0,9)
    #Se já houver atirado nessa posição, gerará outra
    while voce[dano1][dano2] == 'X' or voce[dano1][dano2] == 'O':
        dano1 = aleatorio(0,9)
        dano2 = aleatorio(0,9)
    print('\t\033[1;31mVOCÊ ESTÁ SENDO ATACADO\033[m')
    if voce[dano1][dano2] == 'B':
        voce[dano1][dano2] = 'X'
        pc_ponto += 1
        print('\033[1;31;41mCOMPUTADOR ACERTOU!                                                                           \033[m')
        tabuleiro(voce, '\033[5;37;44m')
        tiro_inimigo()
    else:
        voce[dano1][dano2] = 'O'
        print('\033[1;32;42mCOMPUTADOR ERROU                                                                           \033[m')
        tabuleiro(voce, '\033[5;37;44m')

#Tiro do usuário
def seu_tiro():
    global meu_ponto
    while meu_ponto < 16 and pc_ponto < 16:
        #Placar do jogo
        placar()
        tabuleiro(inimigo, '\033[1;34;41m')
        try:
            horizontal = (int(input('Digite a coordenada horizontal que deseja atacar seu inimigo:\n')))
            vertical = (int(input('Digite a coordenada vertical que deseja atacar seu inimigo:\n')))
        except ValueError:
            print('Dados inseridos incorretamente, tente novamente:\n')
        
        while inimigo[horizontal][vertical] == 'X' or inimigo[horizontal][vertical] == 'O' or inimigo[horizontal][vertical] == 'B':
            horizontal = (int(input('Você ja digitou essas coordenadas, digite uma nova\n Digite a horizontal:\n')))
            vertical = (int(input('Digite a coordenada vertical que deseja atacar seu inimigo:\n')))
        #Se acertar o tiro, marca o x e atira de novo
        if computador[horizontal][vertical] == 'B':
            inimigo[horizontal][vertical] = 'X'
            meu_ponto += 1
            print('\033[1;32;42mVOCÊ ACERTOU!                                                                           \033[m')
            seu_tiro()
        else:
        #Se nao acertar o tiro, computador joga
            print('\033[1;31;41mVOCÊ ERROU!                                                                           \033[m')
            inimigo[horizontal][vertical] = 'O'
            tiro_inimigo()

#Pontuacao e placar do jogo
meu_ponto, pc_ponto = 0, 0
def placar():
    print('\t' + '-'*30 + f'\n\tEU: {meu_ponto}     x     COMPUTADOR: {pc_ponto}\n' + '\t' + '-'*30)


#----------------------CODIGO PRINCIPAL------------------------------------------------------------------------
#Gerar barco inimigo, quantidade é a quantidade de barcos, rand se refere ao numero aleatorio, tamanho é o tamanho do barco
def barcoinimigo(quantidade,rand,tamanho):
    aleatorio1 = aleatorio(0,rand)
    aleatorio2 = aleatorio(0,rand)
    for n in range(quantidade):
        for i in range(tamanho):
            while computador[aleatorio1][aleatorio2] == 'B' or computador[aleatorio1][aleatorio2+i] == 'B' or computador[aleatorio1+i][aleatorio2] == 'B':
                aleatorio1 = aleatorio(0,rand)
                aleatorio2 = aleatorio(0,rand)
        if aleatorio(0,1) == 0:
            for a in range(tamanho):
                computador[aleatorio1][aleatorio2+a] = 'B'
        else:
            for a in range(tamanho):
                computador[aleatorio1+a][aleatorio2] = 'B'

barcoinimigo(3,8,2)
barcoinimigo(2,7,3)
barcoinimigo(1,6,4)

#Posicionar seu tabuleiro
nome = input('''
¶¶¶¶¶¶b.            ¶¶¶             ¶¶¶ ¶¶¶                   ¶¶¶b    ¶¶¶                            ¶¶¶ 
¶¶¶  "¶¶b           ¶¶¶             ¶¶¶ ¶¶¶                   ¶¶¶¶b   ¶¶¶                            ¶¶¶ 
¶¶¶  .¶¶P           ¶¶¶             ¶¶¶ ¶¶¶                   ¶¶¶¶¶b  ¶¶¶                            ¶¶¶ 
¶¶¶¶¶¶¶K.   ¶¶¶¶b.  ¶¶¶¶¶¶  ¶¶¶¶b.  ¶¶¶ ¶¶¶¶¶b.   ¶¶¶¶b.      ¶¶¶Y¶¶b ¶¶¶  ¶¶¶¶b.  ¶¶¶  ¶¶¶  ¶¶¶¶b.  ¶¶¶ 
¶¶¶  "Y¶¶b     "¶¶b ¶¶¶        "¶¶b ¶¶¶ ¶¶¶ "¶¶b     "¶¶b     ¶¶¶ Y¶¶b¶¶¶     "¶¶b ¶¶¶  ¶¶¶     "¶¶b ¶¶¶ 
¶¶¶    ¶¶¶ .d¶¶¶¶¶¶ ¶¶¶    .d¶¶¶¶¶¶ ¶¶¶ ¶¶¶  ¶¶¶ .d¶¶¶¶¶¶     ¶¶¶  Y¶¶¶¶¶ .d¶¶¶¶¶¶ Y¶¶  ¶¶P .d¶¶¶¶¶¶ ¶¶¶ 
¶¶¶   d¶¶P ¶¶¶  ¶¶¶ Y¶¶b.  ¶¶¶  ¶¶¶ ¶¶¶ ¶¶¶  ¶¶¶ ¶¶¶  ¶¶¶     ¶¶¶   Y¶¶¶¶ ¶¶¶  ¶¶¶  Y¶bd¶P  ¶¶¶  ¶¶¶ ¶¶¶ 
¶¶¶¶¶¶¶P"  "Y¶¶¶¶¶¶  "Y¶¶¶ "Y¶¶¶¶¶¶ ¶¶¶ ¶¶¶  ¶¶¶ "Y¶¶¶¶¶¶     ¶¶¶    Y¶¶¶ "Y¶¶¶¶¶¶   Y¶¶P   "Y¶¶¶¶¶¶ ¶¶¶ 

                        $¶     ¶     ¶¢                       
           ¶¶¶¶¶¶¶       ¶¢   ¶   ø¶        ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
          ¶¶    ø¶¶¶      oø  ø  øo        ¶                             INSTRUÇÕES                                  ¶
          ¶7       ¶¶¶      1   1    1o    ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
       ¶¶¶¶¶¶¶       ¶¶¶7        1o¶¶¶ø    ¶                                                                         ¶
       ¶¶¶¶¶¶¶         ¶¶¶¶¶¶¶¶  1         ¶ - Todas as entradas devem ser em letra minúscula e pressionando enter;  ¶ 
     o¶¶¶¶¶¶¶¶¶ø                  o$¢      ¶ - Insira primeiro a entrada horizontal (direita para esquerda)          ¶ 
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶          ¢  1ø   1¶¶o   ¶ - Insira depois a entrada vertical (cima para baixo)                    ¶ 
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶o       1$   ¶          ¶ - X = Acertou o tiro                                                    ¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶       ¶    o¶         ¶ - O = Errou o tiro                                                      ¶   
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶     ¶¶                ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶                        
 ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
  ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
   ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
     ¶¶¶¶¶¶¶¶¶¶¶¶ 
       ¶¶¶¶¶¶¶¶          DIGITE SEU NOME: ''')

while not nome or nome == ' ':
    nome = input('Você deve digitar um nome, insira novamente: ')

#Cumprimenta jogador
print('\n OLÁ', nome, 'VAMOS JOGAR!')
#Apresenta tabuleiro do jogador
tabuleiro(voce, '\033[5;37;44m')
#Posiciona barcos do jogador
barcos()
#Tiro do inimigo primeiro
tiro_inimigo()
#Tiro do player logo após
seu_tiro()

#Se o usuario ganhar
if meu_ponto == 16:
    tabuleiro(inimigo, '\033[1;34;41m')
    print(f'''
¶¶¶     ¶¶¶  .d¶¶¶¶¶b.   .d¶¶¶¶b.  ¶¶¶¶¶¶¶¶¶¶     ¶¶¶     ¶¶¶ ¶¶¶¶¶¶¶¶¶¶ ¶¶¶b    ¶¶¶  .d¶¶¶¶b.  ¶¶¶¶¶¶¶¶¶¶ ¶¶¶     ¶¶¶ ¶¶¶ 
¶¶¶     ¶¶¶ d¶¶P" "Y¶¶b d¶¶P  Y¶¶b ¶¶¶            ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶¶b   ¶¶¶ d¶¶P  Y¶¶b ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
¶¶¶     ¶¶¶ ¶¶¶     ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶            ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶¶¶b  ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
Y¶¶b   d¶¶P ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶¶¶¶¶        Y¶¶b   d¶¶P ¶¶¶¶¶¶¶    ¶¶¶Y¶¶b ¶¶¶ ¶¶¶        ¶¶¶¶¶¶¶    ¶¶¶     ¶¶¶ ¶¶¶ 
 Y¶¶b d¶¶P  ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶             Y¶¶b d¶¶P  ¶¶¶        ¶¶¶ Y¶¶b¶¶¶ ¶¶¶        ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
  Y¶¶o¶¶P   ¶¶¶     ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶              Y¶¶o¶¶P   ¶¶¶        ¶¶¶  Y¶¶¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶     ¶¶¶ Y¶P 
   Y¶¶¶P    Y¶¶b. .d¶¶P Y¶¶b  d¶¶P ¶¶¶               Y¶¶¶P    ¶¶¶        ¶¶¶   Y¶¶¶¶ Y¶¶b  d¶¶P ¶¶¶        Y¶¶b. .d¶¶P  "  
    Y¶P      "Y¶¶¶¶¶P"   "Y¶¶¶¶P"  ¶¶¶¶¶¶¶¶¶¶         Y¶P     ¶¶¶¶¶¶¶¶¶¶ ¶¶¶    Y¶¶¶  "Y¶¶¶¶P"  ¶¶¶¶¶¶¶¶¶¶  "Y¶¶¶¶¶P"  ¶¶¶  
                                                PARABENS, {nome}''')

#Se computador ganhar
elif pc_ponto == 16:
    print(f'''
¶¶¶     ¶¶¶  .d¶¶¶¶¶b.   .d¶¶¶¶b.  ¶¶¶¶¶¶¶¶¶¶     ¶¶¶¶¶¶¶b.  ¶¶¶¶¶¶¶¶¶¶ ¶¶¶¶¶¶¶b.  ¶¶¶¶¶¶¶b.  ¶¶¶¶¶¶¶¶¶¶ ¶¶¶     ¶¶¶ ¶¶¶ 
¶¶¶     ¶¶¶ d¶¶P" "Y¶¶b d¶¶P  Y¶¶b ¶¶¶            ¶¶¶   Y¶¶b ¶¶¶        ¶¶¶   Y¶¶b ¶¶¶  "Y¶¶b ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
¶¶¶     ¶¶¶ ¶¶¶     ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶            ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶    ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
Y¶¶b   d¶¶P ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶¶¶¶¶        ¶¶¶   d¶¶P ¶¶¶¶¶¶¶    ¶¶¶   d¶¶P ¶¶¶    ¶¶¶ ¶¶¶¶¶¶¶    ¶¶¶     ¶¶¶ ¶¶¶ 
 Y¶¶b d¶¶P  ¶¶¶     ¶¶¶ ¶¶¶        ¶¶¶            ¶¶¶¶¶¶¶P"  ¶¶¶        ¶¶¶¶¶¶¶P"  ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶     ¶¶¶ ¶¶¶ 
  Y¶¶o¶¶P   ¶¶¶     ¶¶¶ ¶¶¶    ¶¶¶ ¶¶¶            ¶¶¶        ¶¶¶        ¶¶¶ T¶¶b   ¶¶¶    ¶¶¶ ¶¶¶        ¶¶¶     ¶¶¶ Y¶P 
   Y¶¶¶P    Y¶¶b. .d¶¶P Y¶¶b  d¶¶P ¶¶¶            ¶¶¶        ¶¶¶        ¶¶¶  T¶¶b  ¶¶¶  .d¶¶P ¶¶¶        Y¶¶b. .d¶¶P  "  
    Y¶P      "Y¶¶¶¶¶P"   "Y¶¶¶¶P"  ¶¶¶¶¶¶¶¶¶¶     ¶¶¶        ¶¶¶¶¶¶¶¶¶¶ ¶¶¶   T¶¶b ¶¶¶¶¶¶¶P"  ¶¶¶¶¶¶¶¶¶¶  "Y¶¶¶¶¶P"  ¶¶¶
                                                QUE PENA, {nome}, tente novamente''')
    tabuleiro(voce, '\033[5;37;44m')