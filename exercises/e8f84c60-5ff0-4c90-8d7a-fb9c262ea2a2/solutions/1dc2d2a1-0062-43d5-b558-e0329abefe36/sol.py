def zakoduj_powtorzenia(napis):
    zakodowany_napis = ""
    count = 1

    for i in range(1, len(napis)):
        if napis[i] == napis[i - 1]:
            count += 1
        else:
            if count > 1:
                zakodowany_napis += str(count)
            zakodowany_napis += napis[i - 1]
            count = 1

    if count > 1:
        zakodowany_napis += str(count)
    zakodowany_napis += napis[-1]

    return zakodowany_napis

print(zakoduj_powtorzenia(input()))