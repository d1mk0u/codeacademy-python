def median(lst):
    lst = sorted(lst)
    l = len(lst)
    x = 0
    if l % 2 == 0:
        l = l / 2
        x = (lst[l] + lst[l - 1]) / 2.0
        return x
    else:
        l = l / 2
        x = lst[l]
        return x    
print median([3, 2, 1])
