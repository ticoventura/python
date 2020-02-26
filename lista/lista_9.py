#9) Faça um programa que calcule o aumento de um salário. 
#Ele deve solicitar o valor do salário e a porcentagem de aumento. 
#Mostre o valor do aumento e do novo salário.

sal = float(input("Digite o valor do salário: R$ "))
porc = float(input("Digite o valor da porcentagem de aumento: "))

valor = sal * porc/100
n_sal = sal + valor

print(f"O aumento será de R$ {valor} e o novo salário será R$ {n_sal}")