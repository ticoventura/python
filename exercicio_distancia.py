import math

c1 = input("Digite as primeiras coordenada x e y, separadas por um espaço: ") #x1 y1
c2 = input("Digite as segundas coordenada x e y, separadas por um espaço: ")

x1,y1 = c1.split() #transforma a string em lista: ['x1', 'y1']
x2,y2 = c2.split()

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

d = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(f"A distância entre os pontos digitados é: {d}")