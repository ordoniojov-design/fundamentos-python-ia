# Exercício 1
nome = input("Digite seu nome: ")
print(f"Bem-vindo(a), {nome}!")

# Exercício 2
numero1 = 15
numero2 = 5
print(f"Soma: {numero1 + numero2}")
print(f"Subtração: {numero1 - numero2}")
print(f"Multiplicação: {numero1 * numero2}")
print(f"Divisão: {numero1 / numero2}")

# Exercício 3
"""
A principal diferença entre uma variável de escopo local e uma de escopo global é:
- Variável local: declarada dentro de uma função e só pode ser acessada dentro dela
- Variável global: declarada fora de qualquer função e pode ser acessada em qualquer parte do código
"""

# Exercício 4
saldo = 500.50
saque = 200.25
saldo_final = saldo - saque
print(f"Saldo final: R$ {saldo_final:.2f}")

# Exercício 5
tem_carteira_de_motorista = True
if tem_carteira_de_motorista:
    print("Pode dirigir")
else:
    print("Não pode dirigir")

# Exercício 6
idade_ana = 25
idade_beto = 30
resultado = idade_ana < idade_beto
print(f"Idade de Ana é menor que a de Beto? {resultado}")

# Exercício 7
numero = int(input("Digite um número inteiro: "))
if numero % 2 == 0:
    print(f"O número {numero} é par")
else:
    print(f"O número {numero} é ímpar")

# Exercício 8
chovendo = True
guarda_chuva = False
vai_se_molhar = chovendo and not guarda_chuva
print(f"A pessoa vai se molhar? {vai_se_molhar}")

# Exercício 9
potencia = 2 ** 10
print(f"2 elevado a 10 é: {potencia}")

# Exercício 10
ano = int("2026")
ano += 1
print(f"Ano: {ano}")

# Exercício 11
frase = "   Python é uma linguagem poderosa e estou aprendendo com a DSA   "
frase_sem_espacos = frase.strip()
print(f"Frase sem espaços: {frase_sem_espacos}")

# Exercício 12
frase_maiuscula = frase_sem_espacos.upper()
print(f"Frase em maiúsculas: {frase_maiuscula}")

# Exercício 13
frase_modificada = frase_sem_espacos.replace("poderosa", "incrível")
print(f"Frase modificada: {frase_modificada}")

# Exercício 14
total_caracteres = len(frase_modificada)
print(f"Total de caracteres: {total_caracteres}")

# Exercício 15
palavra_python = frase_modificada[0:6]
print(f"Palavra 'Python': {palavra_python}")

# Exercício 16
compras = ["arroz", "feijão", "macarrão", "carne"]
print(f"Lista de compras: {compras}")

# Exercício 17
compras.append("leite")
print(f"Lista atualizada: {compras}")

# Exercício 18
print(f"Segundo item: {compras[1]}")

# Exercício 19
compras.remove("macarrão")
print(f"Lista final: {compras}")

# Exercício 20
numeros = [1, 2, 3, 4, 5]
print(f"Tamanho da lista: {len(numeros)}")

# Exercício 21
meses = ("Janeiro", "Fevereiro", "Março")
print(f"Tupla meses: {meses}")

# Exercício 22
# Tentativa de adicionar "Abril" à tupla meses
# Isso gerará um erro porque tuplas são imutáveis (não podem ser modificadas após a criação)
# meses.append("Abril")  # Isso causaria AttributeError
print("Tuplas são imutáveis em Python, portanto não é possível adicionar itens após sua criação.")

# Exercício 23
print(f"Primeiro mês: {meses[0]}")

# Exercício 24
filme = {
    "titulo": "O Poderoso Chefão",
    "ano": 1972,
    "diretor": "Francis Ford Coppola"
}
print(f"Dicionário filme: {filme}")

# Exercício 25
print(f"Ano de lançamento: {filme['ano']}")

# Exercício 26
filme["genero"] = "Drama"
print(f"Dicionário com gênero: {filme}")

# Exercício 27
filme["ano"] = 1973
print(f"Dicionário atualizado: {filme}")

# Exercício 28
numeros_lista = [1, 2, 2, 3, 4, 4, 5, 1]
numeros_set = set(numeros_lista)
print(f"Lista original: {numeros_lista}")
print(f"Conjunto sem duplicatas: {numeros_set}")

# Exercício 29
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
intersecao = set_a.intersection(set_b)
print(f"Interseção dos conjuntos: {intersecao}")

# Exercício 30
altura = float(input("Digite sua altura em metros (ex: 1.75): "))
peso = float(input("Digite seu peso em quilogramas (ex: 68.5): "))
imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")
