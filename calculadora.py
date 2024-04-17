import math

#Adição
def adicao(n1, n2):
    adicao = n1 + n2
    return adicao

#Subtração
def subtracao(n1, n2):
    subtracao = n1 - n2
    return subtracao

#Multiplicação
def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    return multiplicacao

#Divisão
def divisao(n1, n2):
    divisao = n1 / n2
    return divisao

#Raiz quadrada
def raiz_quadrada(n1):
    if n1 >= 0:
        raiz = math.sqrt(n1)
    else:
        raiz = "Não foi possível calcular a raiz, escolha um número positivo."
    return raiz

#Maior de 3 números
def maior_tres(n1, n2, n3):
    lista = [n1, n2, n3]
    n1, n2, n3 = sorted(lista)
    return n3

#Média entre 4 números
def media_quatro(n1, n2, n3, n4):
    media = (n1 + n2 + n3 + n4)/ 4
    return media

#Texto do menu
def menu():
    print("-------CALCULADORA-------")
    print("Digite o número correspondente a uma das operações do menu: ")
    print("1. Adição \n2. Subtração \n3. Multiplicação \n4. Divisão \n5. Raiz quadrada \n6. Maior de 3 números \n7. Média de 4 números \n8. Sair")
    print("-------------------------")

#Calculadora
nova = 0  
while not nova == 2:
    menu()
    escolha = input()

    match escolha:
        case "1":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado é: {adicao(n1, n2)}")
        case "2":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado é: {subtracao(n1, n2)}")
        case "3":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado é: {multiplicacao(n1, n2)}")
        case "4":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            print(f"O resultado é: {divisao(n1, n2)}")
        case "5":
            n1 = float(input("Digite o número: "))
            print(f"O resultado é: {raiz_quadrada(n1)}")
        case "6":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            n3 = float(input("Digite o terceiro número: "))
            print(f"O resultado é: {maior_tres(n1, n2, n3)}")
        case "7":
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            n3 = float(input("Digite o terceiro número: "))
            n4 = float(input("Digite o quarto número: "))
            print(f"O resultado é: {media_quatro(n1, n2, n3, n4)}")
        case "8":
            break
    
    print("-------------------------")
    
    #Definir nova operação
    print("Deseja realizar outra operação?")
    nova = int(input("Digite 1. Sim / 2. Não: "))
    print("-------------------------")