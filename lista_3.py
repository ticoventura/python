#3) Faça um programa que peça 2 números inteiros e 1 número real. Calcule e mostre:
a = int(input("Digite um número inteiro: "))
b = int(input("Digite outro número inteiro: "))
c = float(input("Agora, digite um número real: "))

#a) O produto do dobro do primeiro com metade do segundo.
print(f"O produto do dobro de {a} com metade de {b} é: {(2*a) * (b/2)}")

#b) A soma do triplo do primeiro com o terceiro.
print(f"A soma do triplo de {a} com {c} é: {3*a + c}")

#c) O terceiro elevado ao cubo.
print(f"{c} elevado ao cubo é: {c**3}")