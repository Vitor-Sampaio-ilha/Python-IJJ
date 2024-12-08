operacao = input("Digite a operação (soma, subtracao, multiplicacao, divisao): ").lower()
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Verifica qual operação foi escolhida
match operacao:
    case 'soma':
        resultado = num1 + num2
        print(f"Resultado da soma: {resultado}")
    case 'subtracao':
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    case 'multiplicacao':
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    case 'divisao':
        # Evita divisão por zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        # Mensagem para operação inválida
        print("Operação inválida. Tente novamente.")
