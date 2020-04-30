import random

def jogar():
    imprime_msg_abertura()
    
    palavra_secreta = carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida = 0)  
    letras_acertadas = ["_" for letra in palavra_secreta]

    vitoria = jogo(palavra_secreta, letras_acertadas)

    if(vitoria):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

def imprime_msg_abertura():
    print("---------------------------")
    print("Bem vindo ao jogo de Forca!")
    print("---------------------------")

#parâmetro opicional 'nome_aqrquivo'
def carrega_palavra_secreta(nome_arquivo="frutas.txt", primeira_linha_valida=0):
    palavras = []
    with open(nome_arquivo, encoding="utf_8") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(primeira_linha_valida, len(palavras))
    palavra_secreta = palavras[numero].upper()
    # palavra_secreta = str(random.choice(palavras)).upper() //escolhe aleatóriamente uma palavra
    return palavra_secreta

def jogo(palavra_secreta, letras_acertadas):
    enforcou = False
    acertou = False
    erros = 0
    
    while (not enforcou and not acertou):

        chute = validar_chute()

        if (chute in palavra_secreta):
            marca_chute(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)         

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas
        imprimir_letras_acertadas(letras_acertadas)
    return acertou

def imprimir_letras_acertadas(letras_acertadas):
    texto = ""
    for letra in letras_acertadas:
        texto += letra
        texto += "  "
    print(texto)
    print("\n")

def validar_chute():
    validar = True
    while (validar):
        chute = input("Qual letra?").strip().upper()
        if (len(chute) != 1 or str(chute).isnumeric()):
            print("Digite apenas uma letra!!!")
        else:
            validar = False
    return chute

def marca_chute(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[index] = letra 
        index += 1

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__== "__main__"):
    jogar()