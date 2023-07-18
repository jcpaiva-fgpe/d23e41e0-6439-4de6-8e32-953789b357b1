def zakoduj_powtorzenia(napis):
    zakodowany_napis = ""
    count = 1

    for i in range(len(napis) - 1):
        if napis[i] == napis[i + 1]:
            count += 1
        else:
            if count > 1:
                zakodowany_napis += napis[i] + str(count - 1)
            else:
                zakodowany_napis += napis[i]
            count = 1

    if count > 1:
        zakodowany_napis += napis[-1] + str(count)
    else:
        zakodowany_napis += napis[-1]

    return zakodowany_napis

print(zakoduj_powtorzenia(input()))