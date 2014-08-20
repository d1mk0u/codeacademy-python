def remove_duplicates(lst):
    new = []
    for c in lst:
        if c not in new:
            new.append(c)
    return new
print remove_duplicates([1, 1, 2, 3, 4, 4, 5])
