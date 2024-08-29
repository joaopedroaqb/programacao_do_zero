# Exercício 1
# Enunciado: Peça ao usuário para digitar seu nome e, em seguida, exiba uma mensagem de boas-vindas usando print() e .format().
nome = input("Digite o seu nome: ")
print("Olá, {}! Seja bem-vindo(a)!".format(nome))

# Exercício 2
# Enunciado: Solicite ao usuário que informe sua idade e mostre "Você tem [idade] anos."
idade = input("Digite sua idade: ")
print("Você tem {} anos.".format(idade))

# Exercício 3
# Enunciado: Peça ao usuário para digitar dois números e mostre a soma desses números.
num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")
soma = int(num1) + int(num2)  # Convertendo strings para inteiros
print("A soma de {} e {} é {}.".format(num1, num2, soma))

# Exercício 4
# Enunciado: Solicite ao usuário que informe seu peso e altura, calcule o IMC e mostre "Seu IMC é [imc]."
peso = float(input("Digite seu peso (em kg): "))
altura = float(input("Digite sua altura (em metros): "))
imc = peso / (altura ** 2)
print("Seu IMC é {:.2f}.".format(imc))

# Exercício 5
# Enunciado: Peça ao usuário para digitar o nome de um produto e seu preço. Mostre "O produto [produto] custa R$ [preco]."
produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
print("O produto {} custa R$ {:.2f}.".format(produto, preco))

# Exercício 6
# Enunciado: Solicite ao usuário que informe uma frase e exiba "Você digitou: [frase]."
frase = input("Digite uma frase: ")
print("Você digitou: {}".format(frase))

# Exercício 7
# Enunciado: Peça ao usuário para digitar a base e a altura de um triângulo, calcule a área e mostre "A área do triângulo é [area] m²."
base = float(input("Digite a base do triângulo (em metros): "))
altura = float(input("Digite a altura do triângulo (em metros): "))
area = (base * altura) / 2
print("A área do triângulo é {:.2f} m².".format(area))

# Exercício 8
# Enunciado: Solicite ao usuário que digite uma temperatura em Celsius e converta para Fahrenheit. Mostre "[celsius]°C é igual a [fahrenheit]°F."
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("{}°C é igual a {:.1f}°F.".format(celsius, fahrenheit))

# Exercício 9
# Enunciado: Peça ao usuário para digitar a quantidade de horas trabalhadas e o valor por hora. Calcule o salário e mostre "O salário é R$ [salario]."
horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))
salario = horas_trabalhadas * valor_por_hora
print("O salário é R$ {:.2f}.".format(salario))

# Exercício 10
# Enunciado: Solicite ao usuário que informe um número inteiro e mostre o dobro, o triplo e a raiz quadrada desse número.
numero = int(input("Digite um número inteiro: "))
dobro = numero * 2
triplo = numero * 3
raiz_quadrada = numero ** 0.5
print("O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}.".format(numero, dobro, triplo, raiz_quadrada))
