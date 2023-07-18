print("Podaj listę 1:")
lista1 = input().split()

print("Podaj listę 2:")
lista2 = input().split()
print(*sorted(set([elem1 + elem2 for elem1 in lista1 for elem2 in lista2])))