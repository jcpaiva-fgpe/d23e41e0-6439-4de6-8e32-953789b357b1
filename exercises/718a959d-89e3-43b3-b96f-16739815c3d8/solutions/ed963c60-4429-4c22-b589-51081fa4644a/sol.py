def ma_pierwiastek_kwadratowy(liczba):
    if liczba < 0:
        return False
    
    pierwiastek = int(liczba ** 0.5)
    return pierwiastek * pierwiastek == liczba

print(ma_pierwiastek_kwadratowy(int(input())))