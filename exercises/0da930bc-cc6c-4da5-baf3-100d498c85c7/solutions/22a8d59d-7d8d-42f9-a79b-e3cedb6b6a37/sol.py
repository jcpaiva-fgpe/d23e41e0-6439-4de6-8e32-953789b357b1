def uprosc_napis(napis):
    polskie_znaki = "ĄĆĘŁŃÓŚŹŻąćęłńóśźż"
    uproszczenia = "ACELNOSZZacelnoszz"

    napis_uproszczony = ""
    for znak in napis:
        if znak in polskie_znaki:
            indeks = polskie_znaki.index(znak)
            napis_uproszczony += uproszczenia[indeks]
        else:
            napis_uproszczony += znak

    return napis_uproszczony

print(uprosc_napis(input()))