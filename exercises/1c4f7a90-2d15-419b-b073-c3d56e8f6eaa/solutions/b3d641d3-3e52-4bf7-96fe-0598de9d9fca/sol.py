n = {}

while True:
    s = input("Podaj napis:\n")

    if not s:
        break

    l = len(set(s))
    n[s] = l

    max_s = max(n, key=n.get)
    max_l = n[max_s]

    print(f"{max_s} ({max_l})")


print("Koniec programu.")