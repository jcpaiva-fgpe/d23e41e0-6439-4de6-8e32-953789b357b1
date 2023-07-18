def rozstep_listy(lista):
    if not lista:
        return 0

    return max(lista) - min(lista)

print(rozstep_listy(input().split()))