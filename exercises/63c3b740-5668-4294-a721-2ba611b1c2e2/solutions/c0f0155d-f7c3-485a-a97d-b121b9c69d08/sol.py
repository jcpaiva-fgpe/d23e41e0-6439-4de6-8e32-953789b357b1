def zlicz_wyrazy_duza_litera(tekst):
    wyrazy = tekst.split()
    liczba_wyrazow_duza_litera = sum(1 for wyraz in wyrazy if wyraz.isupper())
    print(liczba_wyrazow_duza_litera)

print(zlicz_wyrazy_duza_litera(input()))