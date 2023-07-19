def punkty_w_kosci(rzut):
    rzut.sort()
    rzut_dict = {
        'jedynki': rzut.count(1),
        'dwójki': rzut.count(2) * 2,
        'trójki': rzut.count(3) * 3,
        'czwórki': rzut.count(4) * 4,
        'piątki': rzut.count(5) * 5,
        'szóstki': rzut.count(6) * 6,
        'trzy jednakowe': sum(rzut) if any(rzut.count(x) >= 3 for x in rzut) else 0,
        'cztery jednakowe': sum(rzut) if any(rzut.count(x) >= 4 for x in rzut) else 0,
        'full': 25 if any(rzut.count(x) == 3 for x in rzut) and any(rzut.count(y) == 2 for y in rzut) else 0,
        'mały strit': 30 if sorted(set(rzut)) in [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]] else 0,
        'duży strit': 40 if sorted(set(rzut)) == [1, 2, 3, 4, 5] or sorted(set(rzut)) == [2, 3, 4, 5, 6] else 0,
        'generał': 50 if any(rzut.count(x) == 5 for x in rzut) else 0,
        'szansa': sum(rzut)
    }
    return rzut_dict


print(*list(map(punkty_w_kosci, [[1, 3, 1, 5, 2], [1, 3, 4, 5, 2], [3, 3, 3, 3, 3]])))