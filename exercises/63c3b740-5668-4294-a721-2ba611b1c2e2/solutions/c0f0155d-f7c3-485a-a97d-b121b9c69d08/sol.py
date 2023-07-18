def zlicz_wyrazy_duza_litera(tekst):
    wyrazy = tekst.split()
    liczba_wyrazow_duza_litera = sum(1 for wyraz in wyrazy if any(litera.isupper() for litera in wyraz))
    return liczba_wyrazow_duza_litera

print(zlicz_wyrazy_duza_litera(input()))