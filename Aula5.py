# Exercício 1
# Enunciado: Peça ao usuário para digitar seu nome e sobrenome. Exiba "Seu nome completo é [nome completo]."
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Seu nome completo é {} {}.".format(nome, sobrenome))

# Exercício 2
# Enunciado: Solicite ao usuário que informe a largura e o comprimento de um terreno. Calcule a área e mostre "A área do terreno é [area] m²."
largura = float(input("Digite a largura do terreno (em metros): "))
comprimento = float(input("Digite o comprimento do terreno (em metros): "))
area = largura * comprimento
print("A área do terreno é {:.2f} m².".format(area))

# Exercício 3
# Enunciado: Peça ao usuário para digitar o valor de um produto e a porcentagem de desconto. Calcule o valor com desconto e mostre "O valor com desconto é R$ [valor_final]."
valor_produto = float(input("Digite o valor do produto (em R$): "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
valor_final = valor_produto - (valor_produto * percentual_desconto / 100)
print("O valor com desconto é R$ {:.2f}.".format(valor_final))

# Exercício 4
# Enunciado: Solicite ao usuário que informe um número inteiro e calcule seu quadrado e seu cubo. Mostre "O quadrado de [numero] é [quadrado] e o cubo é [cubo]."
numero = int(input("Digite um número inteiro: "))
quadrado = numero ** 2
cubo = numero ** 3
print("O quadrado de {} é {} e o cubo é {}.".format(numero, quadrado, cubo))

# Exercício 5
# Enunciado: Peça ao usuário para digitar três notas de um aluno e calcule a média. Mostre "A média das notas é [media]."
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print("A média das notas é {:.2f}.".format(media))

# Exercício 6
# Enunciado: Solicite ao usuário que informe a velocidade em km/h e converta para m/s. Mostre "[velocidade] km/h é igual a [velocidade_m_s] m/s."
velocidade_km_h = float(input("Digite a velocidade (em km/h): "))
velocidade_m_s = velocidade_km_h / 3.6
print("{:.1f} km/h é igual a {:.2f} m/s.".format(velocidade_km_h, velocidade_m_s))

# Exercício 7
# Enunciado: Peça ao usuário para digitar o raio de um círculo e calcule a circunferência e a área. Mostre "A circunferência é [circunferencia] e a área é [area]."
import math
raio = float(input("Digite o raio do círculo (em metros): "))
circunferencia = 2 * math.pi * raio
area = math.pi * (raio ** 2)
print("A circunferência é {:.2f} m e a área é {:.2f} m².".format(circunferencia, area))

# Exercício 8
# Enunciado: Solicite ao usuário que informe o nome de um livro e o autor. Exiba "O livro [livro] foi escrito por [autor]."
livro = input("Digite o nome do livro: ")
autor = input("Digite o autor do livro: ")
print("O livro '{}' foi escrito por {}.".format(livro, autor))

# Exercício 9
# Enunciado: Peça ao usuário para informar uma quantidade em reais e converta para dólares. Considere a taxa de câmbio como R$ 5,00 por dólar. Mostre "R$ [reais] é igual a $[dolares]."
reais = float(input("Digite a quantidade em reais (R$): "))
dolares = reais / 5.00  # Considerando a taxa de câmbio de R$ 5,00 por dólar
print("R$ {:.2f} é igual a ${:.2f}.".format(reais, dolares))

# Exercício 10
# Enunciado: Solicite ao usuário que informe dois números e mostre a divisão inteira e o resto da divisão. Exiba "A divisão inteira de [num1] por [num2] é [div_inteira] e o resto é [resto]."
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
div_inteira = num1 // num2
resto = num1 % num2
print("A divisão inteira de {} por {} é {} e o resto é {}.".format(num1, num2, div_inteira, resto))
