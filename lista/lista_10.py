#10) Faça um programa que leia a quantidade de dias, horas, minutos e segundos. Calcule o total em segundos.
d = int(input("Digite a quantidade de dias: "))
h = int(input("Digite a quantidade de horas: "))
m = int(input("Digite a quantidade de minutos: "))
s = int(input("Digite a quantidade de segundos: "))

print(f"O total, em segundos é: {s + m*60 + h*3600 + d*86400}")
