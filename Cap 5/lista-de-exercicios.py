# Exercício 1
nome = input("Digite seu nome: ")
print(f"Olá, {nome}! Seja bem-vindo(a)!")

# Exercício 2
numero1 = 10
numero2 = 5
print(f"Soma: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Divisão: {numero1 / numero2}")

# Exercício 3
# Uma variável de escopo global é declarada fora de qualquer função e pode ser acessada de qualquer lugar do código. 
# Uma variável de escopo local é declarada dentro de uma função e só pode ser acessada dentro daquela função.

# Exercício 4
saldo = 500.50
saque = 200.25
saldo_final = saldo - saque
print(f"Seu saldo final é: R$ {saldo_final:.2f}")

# Exercício 5
tem_carteira_de_motorista = True
if tem_carteira_de_motorista:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# Exercício 6
idade_ana = 25
idade_beto = 30
print(idade_ana < idade_beto)

# Exercício 7
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é PAR.")
else:
    print(f"O número {numero} é ÍMPAR.")

# Exercício 8
chovendo = True
guarda_chuva = False
vai_se_molhar = chovendo and not guarda_chuva
print(f"A pessoa vai se molhar? {vai_se_molhar}")

# Exercício 9
resultado = 2 ** 10
print(f"2 elevado a 10 é: {resultado}")

# Exercício 10
ano_texto = "2026"
ano = int(ano_texto)
ano = ano + 1
print(f"O próximo ano será: {ano}")

# Exercício 11
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "
frase_limpa = frase.strip()
print(frase_limpa)

# Exercício 12
frase_limpa = "Python é uma linguagem poderosa e estou aprendendo com a DSA"
print(frase_limpa.upper())

# Exercício 13
frase_limpa = "Python é uma linguagem poderosa e estou aprendendo com a DSA"
frase_modificada = frase_limpa.replace("poderosa", "incrível")
print(frase_modificada)

# Exercício 14
frase_final = "Python é uma linguagem incrível e estou aprendendo com a DSA"
print(f"A frase tem {len(frase_final)} caracteres.")

# Exercício 15
frase = "Python é uma linguagem incrível"
palavra = frase[0:6]
print(palavra)

# Exercício 16
compras = ["arroz", "feijão", "macarrão", "carne"]
print(compras)

# Exercício 17
compras = ["arroz", "feijão", "macarrão", "carne"]
compras.append("leite")
print(compras)

# Exercício 18
compras = ["arroz", "feijão", "macarrão", "carne"]
print(compras[1])  # O segundo item está no índice 1

# Exercício 19
compras = ["arroz", "feijão", "macarrão", "carne", "leite"]
compras.remove("macarrão")
print(compras)

# Exercício 20
numeros = [1, 2, 3, 4, 5]
print(f"A lista tem {len(numeros)} elementos.")

# Exercício 21
meses = ("Janeiro", "Fevereiro", "Março")
print(meses)

# Exercício 22
# Ocorre um erro (AttributeError: 'tuple' object has no attribute 'append'). 
# Isso acontece porque tuplas são imutáveis, ou seja, não podem ser modificadas após sua criação.

# Exercício 23
meses = ("Janeiro", "Fevereiro", "Março")
print(meses[0])

# Exercício 24
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}
print(filme)

# Exercício 25
filme = {"titulo": "O Poderoso Chefão", "ano": 1972, "diretor": "Francis Ford Coppola"}
print(filme["ano"])

# Exercício 26
filme = {"titulo": "O Poderoso Chefão", "ano": 1972, "diretor": "Francis Ford Coppola"}
filme["genero"] = "Drama"
print(filme)

# Exercício 27
filme = {"titulo": "O Poderoso Chefão", "ano": 1972, "diretor": "Francis Ford Coppola", "genero": "Drama"}
filme["ano"] = 1973
print(filme)

# Exercício 28
lista_numeros = [1, 2, 2, 3, 4, 4, 5, 1]
numeros_unicos = set(lista_numeros)
print(numeros_unicos)

# Exercício 29
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersecao = set_a.intersection(set_b)
print(intersecao)  # Saída: {3, 4}

# Exercício 30
altura_str = input("Digite sua altura em metros (ex: 1.75): ")
peso_str = input("Digite seu peso em kg (ex: 68.5): ")

altura = float(altura_str)
peso = float(peso_str)

imc = peso / (altura * altura)

print(f"Seu IMC é: {imc:.2f}")