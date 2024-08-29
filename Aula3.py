# Exercício 1
# Enunciado: Crie uma variável `nome` e outra `idade`. Use o print() e .format() para exibir "Meu nome é [nome] e eu tenho [idade] anos."
nome = "João"
idade = 25
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Exercício 2
# Enunciado: Declare as variáveis `produto` e `preco`. Mostre a frase "O preço do [produto] é R$ [preco]." usando .format().
produto = "celular"
preco = 1500.50
print("O preço do {} é R$ {:.2f}.".format(produto, preco))

# Exercício 3
# Enunciado: Crie variáveis para `cidade` e `estado`. Exiba "Eu moro em [cidade], [estado]." usando .format().
cidade = "Rio de Janeiro"
estado = "RJ"
print("Eu moro em {}, {}.".format(cidade, estado))

# Exercício 4
# Enunciado: Atribua valores às variáveis `num1` e `num2`, e mostre "A multiplicação de [num1] por [num2] é [resultado]." com .format().
num1 = 8
num2 = 5
resultado = num1 * num2
print("A multiplicação de {} por {} é {}.".format(num1, num2, resultado))

# Exercício 5
# Enunciado: Crie variáveis `nome` e `sobrenome`, e mostre "Seu nome completo é: [nome] [sobrenome]." com .format().
nome = "Ana"
sobrenome = "Silva"
print("Seu nome completo é: {} {}.".format(nome, sobrenome))

# Exercício 6
# Enunciado: Declare as variáveis `quantidade` e `item`. Exiba "Você comprou [quantidade] unidades de [item]." usando .format().
quantidade = 3
item = "cadernos"
print("Você comprou {} unidades de {}.".format(quantidade, item))

# Exercício 7
# Enunciado: Atribua valores às variáveis `altura` e `largura`. Mostre "A área do retângulo é [área] m²." com .format().
altura = 2.5
largura = 4.0
area = altura * largura
print("A área do retângulo é {:.2f} m².".format(area))

# Exercício 8
# Enunciado: Crie variáveis `horas` e `minutos`. Exiba "Agora são [horas] horas e [minutos] minutos." usando .format().
horas = 14
minutos = 30
print("Agora são {} horas e {} minutos.".format(horas, minutos))

# Exercício 9
# Enunciado: Declare `distancia` e `tempo`, e mostre "A velocidade média é [velocidade] km/h." com .format().
distancia = 120  # em km
tempo = 2  # em horas
velocidade = distancia / tempo
print("A velocidade média é {:.1f} km/h.".format(velocidade))

# Exercício 10
# Enunciado: Crie variáveis `saldo_inicial` e `gasto`, e exiba "Seu saldo inicial era R$ [saldo_inicial], e após gastar R$ [gasto], seu saldo é R$ [saldo_final]." usando .format().
saldo_inicial = 1000.00
gasto = 345.50
saldo_final = saldo_inicial - gasto
print("Seu saldo inicial era R$ {:.2f}, e após gastar R$ {:.2f}, seu saldo é R$ {:.2f}.".format(saldo_inicial, gasto, saldo_final))
