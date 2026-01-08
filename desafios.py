#desafio 01

# Recebendo os dados do usuário
dado1 = input("Digite a primeira parte do texto: ")
dado2 = input("Digite a segunda parte do texto: ")

# Realizando a concatenação (unindo os dados)
# Adicionamos um espaço " " entre eles para que não fiquem grudados
resultado = dado1 + " " + dado2

# Exibindo o resultado final
print("A string concatenada é:", resultado)

#desafio 02

# 1. Solicitar uma string como entrada
texto = input("Digite o texto que deseja repetir: ")

# 2. Solicitar um número inteiro como entrada
# Usamos int() para converter a entrada de texto para um número inteiro
vezes = int(input("Digite a quantidade de repetições: "))

# 3. Retornar a string repetida o número de vezes informado
# Em Python, o operador * com strings realiza a repetição
resultado = texto * vezes

# Exibindo o resultado
print("\nResultado da repetição:")
print(resultado)

#desafio 03

# 1. Solicitar dois números como entrada
# Usamos float() para permitir tanto números inteiros quanto decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# 2. Realizar uma operação simples (ex: soma)
resultado = num1 + num2

# 3. Exibir o resultado
print(f"O resultado da soma entre {num1} e {num2} é: {resultado}")