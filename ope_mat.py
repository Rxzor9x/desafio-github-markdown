
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

operacao = input("Digite a operação (+, -, *, /): ")

if operacao == '+':
    resultado = num1 + num2
    print(f"O resultado de {num1} + {num2} é {resultado}")
elif operacao == '-':
    resultado = num1 - num2
    print(f"O resultado de {num1} - {num2} é {resultado}")
elif operacao == '*':
    resultado = num1 * num2
    print(f"O resultado de {num1} * {num2} é {resultado}")
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado de {num1} / {num2} é {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida.")