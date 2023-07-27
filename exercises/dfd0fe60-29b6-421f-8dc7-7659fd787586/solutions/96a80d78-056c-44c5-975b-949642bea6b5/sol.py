def konwertuj_szesnastkowy(napis):
    if napis.startswith("$") and all(c in "0123456789abcdef" for c in napis[1:]):
        szesnastkowy = napis[1:]
        szesnastkowy = szesnastkowy.zfill(4)
        r = "0x" + szesnastkowy
        return r

    return napis

print(konwertuj_szesnastkowy(input()))