def purify(lis):
    new = []
    for q in lis:
        if q == 2 or q % 2 == 0:
            new.append(q)
    return new
print purify([1, 2, 3, 4, 5, 6])
