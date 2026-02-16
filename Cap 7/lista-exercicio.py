# Exercício 1
def dsa_classifica_triangulo(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Triângulo Equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triângulo Isósceles"
    else:
        return "Triângulo Escaleno"

print(f"Lados 5, 5, 5: {dsa_classifica_triangulo(5, 5, 5)}")
print(f"Lados 5, 6, 5: {dsa_classifica_triangulo(5, 6, 5)}")
print(f"Lados 5, 6, 7: {dsa_classifica_triangulo(5, 6, 7)}")

# Exercício 2
def dsa_exibe_tabuada(numero):
    print(f"--- Tabuada do {numero} ---")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

dsa_exibe_tabuada(7)

# Exercício 3
def dsa_alunos_acima_da_media(turma):
    if not turma:
        return "Dicionário de turma vazio."
    soma_notas = sum(turma.values())
    media = soma_notas / len(turma)
    print(f"A média da turma é: {media:.2f}")
    aprovados = []
    for aluno, nota in turma.items():
        if nota > media:
            aprovados.append(aluno)
    return aprovados

notas_turma = {"Ana": 8.5, "Bruno": 6.0, "Carla": 9.5, "Marcelo": 7.0, "Eliane": 5.5}
print(f"Alunos acima da média: {dsa_alunos_acima_da_media(notas_turma)}")

# Exercício 4
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrado_dos_pares = [x ** 2 for x in numeros if x % 2 == 0]
print(f"Lista original: {numeros}")
print(f"Quadrado dos números pares: {quadrado_dos_pares}")

# Exercício 5
def dsa_calcula_imc(peso, altura):
    if altura <= 0:
        return "Altura inválida. Deve ser maior que zero."
    imc = peso / (altura ** 2)
    return imc

meu_imc = dsa_calcula_imc(75, 1.80)
print(f"Seu IMC é: {meu_imc:.2f}")
outro_imc = dsa_calcula_imc(altura=1.65, peso=60)
print(f"O outro IMC é: {outro_imc:.2f}")

# Exercício 6
pessoas = [
    {'nome': 'Carla', 'idade': 32},
    {'nome': 'Bruno', 'idade': 25},
    {'nome': 'Ana', 'idade': 45},
    {'nome': 'Daniel', 'idade': 22}
]
pessoas_ordenadas = sorted(pessoas, key = lambda p: p['idade'])
print("Lista original:")
print(pessoas)
print("\nLista ordenada por idade:")
print(pessoas_ordenadas)

# Exercício 7
def dsa_conta_pares_impares(lista_numeros):
    contagem = {'pares': 0, 'impares': 0}
    for numero in lista_numeros:
        if numero % 2 == 0:
            contagem['pares'] += 1
        else:
            contagem['impares'] += 1
    return contagem

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
resultado = dsa_conta_pares_impares(numeros)
print(f"Na lista, há {resultado['pares']} números pares e {resultado['impares']} números ímpares.")

# Exercício 8
def dsa_filtra_emails_por_dominio(emails, dominio_desejado="gmail.com"):
    return [email for email in emails if email.endswith(f"@{dominio_desejado}")]

lista_emails = [
    "contato@gmail.com", 
    "vendas@yahoo.com", 
    "suporte@gmail.com", 
    "admin@outlook.com"
]
emails_gmail = dsa_filtra_emails_por_dominio(lista_emails)
print(f"E-mails do Gmail: {emails_gmail}")
emails_yahoo = dsa_filtra_emails_por_dominio(lista_emails, dominio_desejado = "yahoo.com")
print(f"E-mails do Yahoo: {emails_yahoo}")

# Exercício 9
frases = [
    "aprendendo a programar",
    "dominando estruturas de dados",
    "funções anônimas são poderosas"
]
frases_modificadas = list(map(lambda f: f.upper() + " EM PYTHON", frases))
for frase in frases_modificadas:
    print(frase)

# Exercício 10
import random

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 20)
    tentativas = 5
    print("Adivinhe o número secreto entre 1 e 20. Você tem 5 tentativas!")
    
    while tentativas > 0:
        print(f"\nVocê tem {tentativas} tentativa(s) restante(s).")
        palpite = int(input("Digite seu palpite: "))
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif palpite < numero_secreto:
            print("Muito baixo!")
        else:
            print("Muito alto!")
        
        tentativas -= 1
    else: 
        print(f"\nFim de jogo! O número secreto era {numero_secreto}.")

jogo_adivinhacao()