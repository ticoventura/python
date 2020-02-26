#5) Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. 
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5.
a = float(input("Digite a primeira nota: "))
b = float(input("Digite a segunda nota: "))
c = float(input("Digite a terceira nota: "))

media = (a*2 + b*3 + c*5)/10

print(f"A média das notas é: {media}")