import random

def jogar():
    #variáveis
    total_de_pontos = 1000
    perda_pontos_rodada = 0
    pontuacao_atual = 1000
    total_de_tentativas = 0
    fator_bonus_dificuldade = 0
    rodada = 1
    numero_secreto = random.randint(1,100)
    # numero_secreto = 50
    acertou = False
    definiu_nivel = False

    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    # validação da escolha de nível
    while definiu_nivel == False:
        nivel_str = input("Define o nível: ")

        if str(nivel_str).isnumeric():
            nivel = int(nivel_str)
        else:
            print("Você deve escolher o nível!!!")
            continue
        if nivel == 1:
            definiu_nivel = True
            total_de_tentativas = 20
            fator_bonus_dificuldade = 1
        elif nivel == 2:
            definiu_nivel = True
            total_de_tentativas = 10
            fator_bonus_dificuldade = 1.25
        elif nivel == 3:
            definiu_nivel = True
            total_de_tentativas = 5
            fator_bonus_dificuldade = 1.5
        else:
            print("Você deve escolher o nível!!!")

    #Cálculo da perda de pontos por rodada
    perda_pontos_rodada = total_de_pontos / total_de_tentativas

    #Rodadas
    for rodada in range(1,total_de_tentativas + 1):
        print("Tentativa: {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("você digitou:",chute_str)

        #Validação do chute
        if not str(chute_str).isnumeric():
            print("Você deve digitar um número entre 1 e 100!")
            pontuacao_atual -= perda_pontos_rodada
            continue

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            pontuacao_atual -= perda_pontos_rodada
            continue

        #lógica de acerto/erro
        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou): 
            print("parabéns, você acertou")
            break
        elif (maior):
            print("você errou! O seu chute foi maior que o número secreto.")
            pontuacao_atual -= perda_pontos_rodada
        elif (menor):
            print("você errou! O seu chute foi menor que o número secreto.")
            pontuacao_atual -= perda_pontos_rodada

    #Imprime o término das tentativas apenas caso tenha perdido
    if (not acertou):
        print("acabou suas tentativas")

    #Fim do jogo
    print("fim do jogo")
    print("Pontuação:", pontuacao_atual * fator_bonus_dificuldade)

if(__name__== "__main__"):
    jogar()
