#2) Faça um programa que peça 4 notas bimestrais e mostre a média. 
notas = input("Digite as 4 notas bimestrais separadas por um espaço: ")

n1,n2,n3,n4 = notas.split()

n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

media = (n1+n2+n3+n4)/4

print(f"A média das notas é: {media}")