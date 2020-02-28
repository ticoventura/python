n1,n2,n3 = input("Digite 3 números inteiros, separados por espaço: ").split()

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

if n1 < n2 > n3:
    if n1 < n3:
        print(f"Ordem crescente: {n1}\n{n3}\n{n2}")
    else:
        print(f"Ordem crescente: {n3}\n{n1}\n{n2}")
elif n1 < n3 > n2:
    if n1 < n2:
        print(f"Ordem crescente: {n1}\n{n2}\n{n3}")
    else:
        print(f"Ordem crescente: {n2}\n{n1}\n{n3}")
else:
    if n2 < n3:
        print(f"Ordem crescente: {n2}\n{n3}\n{n1}")
    else:
        print(f"Ordem crescente: {n3}\n{n2}\n{n1}")   