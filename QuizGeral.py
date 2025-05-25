questoes = (("Qual elemento químico tem o símbolo Mg ?: "),
            ("Qual é o maior país do mundo ?:"),
            ("Qual é o maior continente do mundo ?:"),
            ("Quem é o homem mais rápido do mundo ?: "))
opcoes = (("A) Magnésio", "B) Mercúrio", "C) Molibdênio", "D) Manganês"),
          ("A) China", "B) Brasil", "C) Rússia", "D) Estados Unidos"),
          ("A) Antártida", "B) América do Sul", "C) África", "D) Ásia"),
          ("A) Noah Lyles", "B) Cristiano Ronaldo", "C) Usain Bolt", "D) Lebron James"))

resp = ("A", "C", "D", "C")
escolhas = []
pont = 0
num_quest = 0

for questao in questoes:
    print("---------------------")
    print(questao)
    for opcao in opcoes[num_quest]:
        print(opcao)
    resposta = input("Digite a letra da sua resposta (A, B, C ou D): ").upper()
    escolhas.append(resposta)
    if resposta == resp[num_quest]:
        pont += 1
        print("Correto")
    else:
        print("Incorreto")
        print(f"A resposta correta é: {resp[num_quest]}")
    num_quest += 1

print("---------------------")
print("     RESULTADOS      ")
print("---------------------")

print("Respostas: ", end="")
for i in resp:
    print(i, end=" ")
print()

print("Escolhas: ", end=" ")
for i in escolhas:
    print(i, end=" ")
print()

pont = int(pont/len(questoes)*100)
print(f"Sua pontuação é: {pont}%")