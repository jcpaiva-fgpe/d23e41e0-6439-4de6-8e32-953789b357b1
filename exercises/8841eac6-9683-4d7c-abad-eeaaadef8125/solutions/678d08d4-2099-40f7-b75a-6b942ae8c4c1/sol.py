def najdluzsza_wspolna_sekwencja(*napisy):
    if not napisy:
        return ""

    shortest_napis = min(napisy, key=len)
    max_sekwencja = ""

    for i in range(len(shortest_napis)):
        for j in range(i + 1, len(shortest_napis) + 1):
            sekwencja = shortest_napis[i:j]
            if all(sekwencja in napis for napis in napisy):
                if len(sekwencja) > len(max_sekwencja):
                    max_sekwencja = sekwencja

    return max_sekwencja

# Przykłady użycia funkcji:
przyklad1 = najdluzsza_wspolna_sekwencja("a", "b", "c")
przyklad2 = najdluzsza_wspolna_sekwencja("rok", "bok", "ćwok")
przyklad3 = najdluzsza_wspolna_sekwencja("dzisiejszy", "dzisiaj", "niedzisiejszy")
przyklad4 = najdluzsza_wspolna_sekwencja("pogoda", "niepogoda", "pagoda", "wygoda", "zagroda", "broda", "oda", "woda")
przyklad5 = najdluzsza_wspolna_sekwencja("pogoda", "niepogoda", "x")

print(przyklad1)
print(przyklad2)
print(przyklad3)
print(przyklad4)
print(przyklad5)