def reverse(x):
    lst = []
    for l in x:
        lst.append(l)
    for b in range(0, len(lst)):
        letter = len(lst)
        while letter > 0:
            letter -=  1
            print lst[letter],        
print reverse("Python!")
