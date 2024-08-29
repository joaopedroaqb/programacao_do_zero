# Exercício 11
# Enunciado: Crie variáveis `nome` e `curso`. Use o print() e .format() para exibir "Meu nome é [nome] e estou estudando [curso]."
nome = "Lucas"
curso = "Programação"
print("Meu nome é {} e estou estudando {}.".format(nome, curso))

# Exercício 12
# Enunciado: Declare as variáveis `temperatura` e `cidade`. Mostre "A temperatura em [cidade] é de [temperatura]°C." usando .format().
temperatura = 30.5
cidade = "Fortaleza"
print("A temperatura em {} é de {:.1f}°C.".format(cidade, temperatura))

# Exercício 13
# Enunciado: Crie variáveis `nome_do_filme` e `ano`. Exiba "O filme [nome_do_filme] foi lançado em [ano]." com .format().
nome_do_filme = "Inception"
ano = 2010
print("O filme {} foi lançado em {}.".format(nome_do_filme, ano))

# Exercício 14
# Enunciado: Declare as variáveis `quantidade` e `preco_unitario`. Exiba "O total é R$ [total] para [quantidade] itens." usando .format().
quantidade = 6
preco_unitario = 12.50
total = quantidade * preco_unitario
print("O total é R$ {:.2f} para {} itens.".format(total, quantidade))

# Exercício 15
# Enunciado: Atribua valores às variáveis `altura` e `peso`. Exiba "Seu IMC é [imc]." usando .format(), com o cálculo do IMC (peso / altura^2).
altura = 1.75
peso = 68
imc = peso / (altura ** 2)
print("Seu IMC é {:.2f}.".format(imc))

# Exercício 16
# Enunciado: Crie variáveis `marca`, `modelo` e `ano`. Mostre "Você dirige um [marca] [modelo] do ano [ano]." com .format().
marca = "Toyota"
modelo = "Corolla"
ano = 2020
print("Você dirige um {} {} do ano {}.".format(marca, modelo, ano))

# Exercício 17
# Enunciado: Declare variáveis `base` e `expoente`. Exiba "O resultado de [base] elevado a [expoente] é [resultado]." usando .format().
base = 3
expoente = 4
resultado = base ** expoente
print("O resultado de {} elevado a {} é {}.".format(base, expoente, resultado))

# Exercício 18
# Enunciado: Crie variáveis `horas_trabalhadas` e `valor_hora`. Exiba "O salário é R$ [salario] para [horas_trabalhadas] horas trabalhadas." usando .format().
horas_trabalhadas = 40
valor_hora = 25.00
salario = horas_trabalhadas * valor_hora
print("O salário é R$ {:.2f} para {} horas trabalhadas.".format(salario, horas_trabalhadas))

# Exercício 19
# Enunciado: Atribua valores às variáveis `largura`, `comprimento` e calcule a área e o perímetro. Exiba "Área: [area] m², Perímetro: [perimetro] m." usando .format().
largura = 5
comprimento = 10
area = largura * comprimento
perimetro = 2 * (largura + comprimento)
print("Área: {} m², Perímetro: {} m.".format(area, perimetro))

# Exercício 20
# Enunciado: Crie variáveis `nome_do_cliente` e `produto_comprado`, e exiba "Obrigado, [nome_do_cliente], por comprar [produto_comprado]!" com .format().
nome_do_cliente = "Mariana"
produto_comprado = "notebook"
print("Obrigado, {}, por comprar {}!".format(nome_do_cliente, produto_comprado))
