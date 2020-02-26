t = int(input("Digite o tempo em segundos: "))
h = t // 3600
m = (t % 3600) // 60
s = t % 60
print(f"O tempo digitado, em horas, é: {h}:{m}:{s}")