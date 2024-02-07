import random

print("Bem vindo ao jogo de adivinhação")
dificuldade = input("Qual a dificuldade do jogo é do seu desejo? (Facil/medio/dificil/insano): ")

while dificuldade.lower() not in ("facil","medio","dificil","insano"):
    print("Dificuldade inválida, (Facil/medio/dificil/insano)")
    dificuldade = input("Qual a dificuldade do jogo é do seu desejo? (Facil/medio/dificil/insano): ")
   
    
if dificuldade == "facil":
    numero_sorteado = random.randint(1,10)
    palpite_jogador = int(input("Dê o seu palpite "))

    auxilio_inferior = 1
    auxilio_superior = 10

    while palpite_jogador is not numero_sorteado:
        if palpite_jogador > 10 or palpite_jogador < 1:
            palpite_jogador = int(input("O numero digitado foi inválido. O número tem que estar entre 1 e 10. Digite um outro palpite, seguindo a regra\n"))

        elif palpite_jogador > numero_sorteado:
            if(auxilio_superior > palpite_jogador):
                auxilio_superior = palpite_jogador
            palpite_jogador = int(input(f"Xii chutou alto. Tente novamente. Dica: O número sorteado é menor do que o seu palpite e está entre {auxilio_inferior} e {palpite_jogador}\n"))

        elif palpite_jogador < numero_sorteado:
            if(auxilio_inferior < palpite_jogador):
                auxilio_inferior = palpite_jogador
            palpite_jogador = int(input(f"Xii chutou baixo. Tente novamente. Dica: O número sorteado é maior do que o seu palpite e está entre {palpite_jogador} e {auxilio_superior}\n"))
        


    print("Parabéns, você acertou o número sorteado")

elif dificuldade == "medio":
    numero_sorteado = random.randint(1,50)
    palpite_jogador = int(input("Dê o seu palpite "))

    while palpite_jogador is not numero_sorteado:
        if palpite_jogador > 50 or palpite_jogador < 1:
            palpite_jogador = int(input("O numero digitado foi inválido. O número tem que estar entre 1 e 50. Digite um outro palpite, seguindo a regra\n"))

        elif palpite_jogador > numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou alto. Tente novamente. Dica: O número sorteado é menor do que o seu palpite e está entre 1 e {palpite_jogador}\n"))

        elif palpite_jogador < numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou baixo. Tente novamente. Dica: O número sorteado é maior do que o seu palpite e está entre {palpite_jogador} e 50\n"))
        


    print("Parabéns, você acertou o número sorteado")

elif dificuldade == "dificil":
    numero_sorteado = random.randint(1,100)
    palpite_jogador = int(input("Dê o seu palpite "))

    while palpite_jogador is not numero_sorteado:
        if palpite_jogador > 100 or palpite_jogador < 1:
            palpite_jogador = int(input("O numero digitado foi inválido. O número tem que estar entre 1 e 100. Digite um outro palpite, seguindo a regra\n"))

        elif palpite_jogador > numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou alto. Tente novamente. Dica: O número sorteado é menor do que o seu palpite e está entre 1 e {palpite_jogador}\n"))

        elif palpite_jogador < numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou baixo. Tente novamente. Dica: O número sorteado é maior do que o seu palpite e está entre {palpite_jogador} e 100\n"))
        


    print("Parabéns, você acertou o número sorteado")

elif dificuldade == "insano":
    numero_sorteado = random.randint(1,1000)
    palpite_jogador = int(input("Dê o seu palpite "))

    while palpite_jogador is not numero_sorteado:
        if palpite_jogador > 1000 or palpite_jogador < 1:
            palpite_jogador = int(input("O numero digitado foi inválido. O número tem que estar entre 1 e 1000. Digite um outro palpite, seguindo a regra\n"))

        elif palpite_jogador > numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou alto. Tente novamente. Dica: O número sorteado é menor do que o seu palpite e está entre 1 e {palpite_jogador}\n"))

        elif palpite_jogador < numero_sorteado:
            palpite_jogador = int(input(f"Xii chutou baixo. Tente novamente. Dica: O número sorteado é maior do que o seu palpite e está entre {palpite_jogador} e 1000\n"))
        


    print("Parabéns, você acertou o número sorteado")