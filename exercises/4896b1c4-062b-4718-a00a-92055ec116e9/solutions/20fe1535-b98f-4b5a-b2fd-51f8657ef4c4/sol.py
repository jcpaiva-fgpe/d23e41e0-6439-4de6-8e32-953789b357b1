def rotuj_cyfry_w_prawo(liczba):
    liczba_str = str(liczba)
    ostatnia_cyfra = liczba_str[-1]
    przekształcona_liczba = ostatnia_cyfra + liczba_str[:-1]
    
    return int(przekształcona_liczba)

print(rotuj_cyfry_w_prawo(int(input())))