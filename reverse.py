def reverse(x):
    result = ""
    l = (len(x)) - 1
    while l >= 0:
        result += x[l]
        l -= 1
        print result
    return result
print reverse("Python!")
