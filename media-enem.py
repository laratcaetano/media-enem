"""
Algoritmo que calcula a média simples das notas do Enem,
e verifica se o estudante cumpre alguns dos requisitos para participar do SISU, PROUNI e FIES.
"""

nome = input("Qual o seu nome? ")
print(f"{nome}, informe as suas notas do Enem para calcularmos a sua média simples.")

print("\n##########################################################################")
redacao = float(input("Redação: "))
linguagens = float(input("Linguagens, Códigos e suas Tecnologias: "))
humanas = float(input("Ciências Humanas e suas Tecnologias: "))
matematica = float(input("Matemática e suas Tecnologias: "))
natureza = float(input("Ciências da Natureza e suas Tecnologias: "))
print("##########################################################################")

media = (redacao + linguagens + humanas + matematica + natureza) / 5
print(f"\nSua média é: {media}")

if redacao == 0 and media <= 450:
    print("\nEstude mais! Você zerou a redação e a sua média foi inferior a 450 pontos.")
elif redacao == 0:
    print("\nEstude mais! Você zerou a redação.")
elif media <= 450:
    print("\nEstude mais! A sua média foi inferior a 450 pontos.")
else:
    print("\nParabéns! Você já cumpre três requisitos para participar do SISU, PROUNI e/ou FIES:\n"
          "1 - Ter feito o Enem. 2 - Não ter zerado a redação. 3. Ter obtido média igual ou superior a 450 pontos.\n"
          "Verifique os outros requisitos e se inscreva. ;)")
