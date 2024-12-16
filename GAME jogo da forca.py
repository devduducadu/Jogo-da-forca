import random
#PASSO A PASSO JOGO DA FORCA
# PASSO 1: criar uma lista de palavras.
# PASSO 2: dizer quantas letras tem a palavra.
# PASSO 3: fazer o usuario adivinhar a palavra colocando um limite de erros e quantas jogadas ele tem.
# PASSO 4: permitir que enquanto o usuario não atingir os 6 erros ele possa jogar novamente(loop).
# PASSO 5: mostrar o feedback ao usuario de acerto e erro.
# PASSO 6: feedback de derrota e vitoria.

def escolher_palavra(lista_de_palavras):
    return random.choice(lista_de_palavras)

def contar_letras(palavra):
    return len(palavra)

def verificar_letra_digitada(letra_digitada, letras_adivinhadas):
    if letra_digitada in letras_adivinhadas:
        return False
    else:
        letras_adivinhadas.add(letra_digitada)
        return True

def verificar_vitoria(palavra, letras_adivinhadas):
    return all(letra in letras_adivinhadas for letra in palavra)

def jogo_da_forca():
    # PASSO 1: criar uma lista de palavras
    lista_de_palavras = ['gêmeo', 'polícia', 'lubrificante']

    # PASSO 2: escolher uma palavra aleatória da lista
    palavra_aleatoria = escolher_palavra(lista_de_palavras)

    # Contar quantas letras tem a palavra
    contagem = contar_letras(palavra_aleatoria)
    print(f'A palavra tem {contagem} letras.')

    # PASSO 3: inicializar variáveis
    jogadas_usuario = 0
    erros = 6
    letras_adivinhadas = set()

    # PASSO 4: loop principal do jogo
    while jogadas_usuario < erros:
        letra_digitada = input('Digite uma letra: ').lower()

        # Verifica se a letra já foi digitada antes
        if not verificar_letra_digitada(letra_digitada, letras_adivinhadas):
            print('Você já tentou essa letra. Tente outra.')
            continue

        # PASSO 5: verificar se a letra digitada está na palavra
        if letra_digitada in palavra_aleatoria:
            print('Letra correta!')
        else:
            print('Letra incorreta!')
            jogadas_usuario += 1

        # PASSO 6: verificar se todas as letras foram adivinhadas corretamente
        if verificar_vitoria(palavra_aleatoria, letras_adivinhadas):
            print(f'\nParabéns! Você descobriu a palavra "{palavra_aleatoria}". Você venceu!')
            return

    # Verifica se o número de jogadas do usuário excedeu o número de erros permitidos
    if jogadas_usuario >= erros:
        print(f'\nVocê perdeu! A palavra correta era "{palavra_aleatoria}".')

# Inicia o jogo da forca
jogo_da_forca()
