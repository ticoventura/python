num = int(input("Digite um número: "))

#if num>=0 and num<=50:
if 0 <= num <= 50:
    print("Intervalo [0, 50]")
#else: 
    #if num>50 and num<=100:
        #print("Intervalo [51, 100]")
    #else:
        #print("Fora do Intervalo")
elif 51 <= num <= 100:
    print("Intervalo [51, 100]")
else:
    print("Fora do Intervalo")