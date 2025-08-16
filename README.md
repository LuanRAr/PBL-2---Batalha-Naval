# PBL-2---Batalha-Naval
Criação de um jogo de batalha naval utilizando alguns princípios básicos de Python. Alguns recursos foram proibidos.

📌 Funcionalidades
Tabuleiro 10x10 para cada jogador.
Posicionamento manual dos barcos do jogador.
Posicionamento automático e aleatório dos barcos do computador.
Sistema de pontuação e placar exibido a cada rodada.
Cores no terminal para diferenciar acertos e erros.
Condições de vitória e derrota com mensagens finais personalizadas.

🎮 Como jogar
Clone ou baixe este repositório.
Certifique-se de ter o Python 3.10 (ou superior) instalado.
Execute o arquivo principal no terminal:
python batalha_naval.py
Digite seu nome quando solicitado.
Posicione seus barcos (BB, BBB e BBBB) informando:
A coordenada horizontal (x) → da esquerda para a direita.
A coordenada vertical (y) → de cima para baixo.
A orientação do barco: h (horizontal) ou v (vertical).
Após o posicionamento, o jogo inicia automaticamente:
Você e o computador atiram alternadamente.
X → acerto.
O → erro.
O primeiro a atingir 16 acertos vence.

📊 Placar
EU → Pontuação do jogador.
COMPUTADOR → Pontuação da máquina.

🛠 Estrutura do código
cria_matriz() → cria os tabuleiros.
posicionar() → posiciona barcos do jogador.
barcos() → organiza os navios do jogador.
barcoinimigo() → posiciona barcos do computador.
seu_tiro() → jogada do usuário.
tiro_inimigo() → jogada do computador.
placar() → mostra o resultado parcial.

🏆 Condições de vitória
O jogo termina quando:
Você atinge 16 pontos → Vitória.
O computador atinge 16 pontos → Derrota.
