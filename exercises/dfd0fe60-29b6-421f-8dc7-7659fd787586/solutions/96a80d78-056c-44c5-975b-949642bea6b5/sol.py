def konwertuj_szesnastkowy(napis):
    if napis.startswith("$") and all(c in "0123456789abcdef" for c in napis[1:]):
        szesnastkowy = napis[1:]
        szesnastkowy = szesnastkowy.zfill(4)
        return "0x" + szesnastkowy

    return napis

print(konwertuj_szesnastkowy(input()))