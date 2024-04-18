#Entradas
print("------JOGO DE ADIVINHAÇÃO------")
print("Escolha um intervalo entre dois números:")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
print("Agora pense em um número dentro desse intervalo, vou tentar adivinhar!")

#Controle
numero_encontrado = False

#Busca binária
while not numero_encontrado:

    #Para dividir ao meio as possibilidades
    verificador_numero = int((n1 + n2) / 2)

    #Confirmação com o usuário
    maior_que = input(f"O número que você pensou é maior que {verificador_numero}? Digite SIM ou NÃO: ").upper()

    #Validação da resposta do usuário, reajusta o valor mínimo ou máximo
    if maior_que == "SIM":
        n1 = verificador_numero + 1
    else:
        n2 = verificador_numero

    #Condição de adivinhação do número
    if n1 == n2:
        numero_encontrado = True
        print(f"O seu número é {n1}!")