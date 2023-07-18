def konwertuj_na_zwykly_ulamek(liczba):
    def najblizszy_mianownik(liczba):
        for mianownik in range(1, 10):
            zaokraglona = round(liczba * mianownik)
            if abs(liczba - zaokraglona / mianownik) < 0.0001:
                return mianownik
        return 9

    mianownik = najblizszy_mianownik(liczba)
    licznik = int(round(liczba * mianownik))

    if licznik == 0:
        return "0/9"
    elif licznik == mianownik:
        return "9/9"
    else:
        return f"{licznik}/{mianownik}"

print(konwertuj_na_zwykly_ulamek(float(input())))