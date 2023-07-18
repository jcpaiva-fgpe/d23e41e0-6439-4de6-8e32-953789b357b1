def konwertuj_na_zwykly_ulamek(liczba):
    def najwiekszy_wspolny_dzielnik(a, b):
        while b:
            a, b = b, a % b
        return a

    def skroc_ulamek(licznik, mianownik):
        wspolny_dzielnik = najwiekszy_wspolny_dzielnik(licznik, mianownik)
        return licznik // wspolny_dzielnik, mianownik // wspolny_dzielnik

    mianownik = 9
    licznik = int(round(liczba * mianownik))

    if licznik == 0:
        return "0/9"
    elif licznik == mianownik:
        return "9/9"
    else:
        licznik, mianownik = skroc_ulamek(licznik, mianownik)
        return f"{licznik}/{mianownik}"

print(konwertuj_na_zwykly_ulamek(float(input())))