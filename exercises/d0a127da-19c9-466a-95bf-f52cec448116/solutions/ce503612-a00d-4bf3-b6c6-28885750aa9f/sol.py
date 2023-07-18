def rozstep_listy(lista):
    if not lista:
        return 0

    return max(lista) - min(lista)

# Wywołując funkcję użyj zmiennej zadanie.
zadanie = list(map(int, input().split()))


print(rozstep_listy(zadanie))