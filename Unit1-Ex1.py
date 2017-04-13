import itertools

class Unit1_Ex1:
    def __init__(self): pass

    def yieldAllCombos(self, items):
        n = len(items)
        for i in range(3**n):
            combo1 = []
            combo2 = []
            for j in range(n):
                idx = (i // (3**j)) % 3
                if idx == 1:
                    combo1.append(items[j])
                elif idx == 2:
                    combo2.append(items[j])
            yield (combo1, combo2)

    def powerSet(self, items):
        return itertools.chain.from_iterable(itertools.combinations(items, r) for r in range(len(items) + 1))

a = Unit1_Ex1()
for i in a.powerSet([1, 2, 3]):
    print i
