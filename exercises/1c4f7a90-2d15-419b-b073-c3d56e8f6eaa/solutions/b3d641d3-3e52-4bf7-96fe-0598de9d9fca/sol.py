n = {}

while True:
    print("Podaj napis:")
    s = input()

    if not s:
        break

    l = len(set(s))
    n[s] = l

    max_s = max(n, key=n.get)
    max_l = n[max_s]
    
    print(str(max_s) +' ('+ str(max_l)+")")


print("Koniec programu.")
