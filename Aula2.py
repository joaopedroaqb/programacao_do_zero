# Exercício 1
# Enunciado: Crie uma variável chamada `nome` e atribua o seu nome a ela. Em seguida, use o print() para exibir o valor da variável.
nome = "Seu Nome"
print(nome)

# Exercício 2
# Enunciado: Crie uma variável `idade` e atribua a sua idade a ela. Mostre o valor usando print().
idade = 25  # Altere para sua idade
print(idade)

# Exercício 3
# Enunciado: Declare duas variáveis, `a` e `b`, atribua valores numéricos a elas, e mostre a soma dos valores.
a = 10
b = 5
print(a + b)

# Exercício 4
# Enunciado: Crie uma variável chamada `cidade` e atribua o nome da sua cidade. Use print() para exibir a frase "Eu moro em [cidade]".
cidade = "São Paulo"
print("Eu moro em", cidade)

# Exercício 5
# Enunciado: Atribua os valores 7 e 3 às variáveis `x` e `y`, respectivamente. Exiba a subtração de `x` menos `y`.
x = 7
y = 3
print(x - y)

# Exercício 6
# Enunciado: Crie uma variável `pi` e atribua a ela o valor de 3.14159. Mostre o valor de pi multiplicado por 2.
pi = 3.14159
print(pi * 2)

# Exercício 7
# Enunciado: Declare uma variável `mensagem` e atribua um texto de sua escolha. Mostre o texto 3 vezes seguidas usando o print().
mensagem = "Python é divertido! "
print(mensagem * 3)

# Exercício 8
# Enunciado: Crie variáveis `base` e `altura`, atribua valores a elas, e mostre o cálculo da área de um retângulo (base * altura).
base = 10
altura = 5
print(base * altura)  # Área do retângulo

# Exercício 9
# Enunciado: Declare uma variável `saldo` com um valor inicial de 1000. Subtraia 250 e mostre o saldo atualizado.
saldo = 1000
saldo = saldo - 250
print(saldo)

# Exercício 10
# Enunciado: Crie uma variável `nome_completo` combinando as variáveis `primeiro_nome` e `sobrenome`. Mostre o nome completo.
primeiro_nome = "João"
sobrenome = "Pedro"
nome_completo = primeiro_nome + " " + sobrenome
print(nome_completo)





# CODIGO JOÃO PEDRO


print("Exercicio 1: 'nome'\nExercicio 2: 'idade'\nExercicio 3: 'A e B'\nExercicio 4: 'Cidade'\nExercicio 5: 'X e Y'\nExercicio 6: 'pi'\nExercicio 7: 'mensagem'\nExercicio 8: 'Base x Altura'\nExercicio 9: 'saldo'\nExercicio 10: 'nome completo' ")
opc = int(input("Digite qual Exercicio você quer: "))

if opc == 1:
    print("Você escolheu opção 1")
    nome = str(input("Digite seu nome: "))
    print("Seu nome é {}".format(nome))

elif opc == 2:
    print("Você escolheu opção 2")
    idade = int(input("Digite sua idade: "))
    print("Sua idade é: ", idade, "anos")

elif opc == 3:
    print("Você escolheu opção 3")
    a = int(input("Digite o valor de 'a': "))
    b = int(input("Digite o valor de 'b': "))
    print("A soma de a + b = {}".format(a+b))

elif opc == 4:
    print("Você escolheu opção 4")
    cidade = str(input("Digite o nome de uma cidade: "))
    print("A cidade que você digitou foi '{}'".format(cidade))

elif opc == 5:
    print("Você escolheu opção 5")
    x = int(input("Digite o valor de 'x': "))
    y = int(input("Digite o valor de 'y': "))
    print("A soma de a + b = {}".format(x-y))

elif opc == 6:
    print("Você escolheu opção 6")
    pi = 3.14159
    multi = int(input("Escolha a quantidade de vezes que você quer multiplicar 'pi': "))
    print("{} x pi = {}".format(multi, multi*pi))

elif opc == 7:
    print("Você escolheu opção 7")
    mensagem = input("Escreva uma frase para ser repetida 3x: ")
    print(mensagem*3)

elif opc == 8:
    print("Você escolheu opção 8")
    base = float(input("Digite o valor da base do retangulo: "))
    alt = float(input("Digite o valor da altura do retangulo: "))
    print("A area do retangulo é de: {}".format(base*alt))

elif opc == 9:
    print("Você escolheu opção 9")
    saldo = float(input("Digite o saldo atual: "))
    retirada = float(input("Digite o valor da retirada que deseja fazer: "))
    print("Seu saldo é de {}, você deseja retirar {}, o saldo final ficará de {} reais".format(saldo, retirada, saldo-retirada))

elif opc == 10:
    print("Você escolheu opção 10")
    nome1 = str(input("Digite seu nome: "))
    sobrenome = str(input("Digite seu sobrenome: "))
    print("Seu nome completo é: {}".format(nome1 + sobrenome ))

else:
    print("Opção invalida, escolha uma opção correta")
