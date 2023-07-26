print("Pomyśl liczbę 1-99 i wciśnij enter.")
w = input()

dolna_granica = 1
gorna_granica = 99
liczba_prob = 0

while True:
   
    liczba_prob += 1
    propozycja = (dolna_granica + gorna_granica) // 2

    print(f"Czy to {propozycja}?")
    odpowiedz = input()

    if odpowiedz == "-":
        gorna_granica = propozycja - 1
    elif odpowiedz == "+":
        dolna_granica = propozycja + 1
    else:
        print(f"Zgadłem za {liczba_prob} razem.")
        break
