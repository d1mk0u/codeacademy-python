#answer = raw_input("Insert a string:")
def anti_vowel(text):
    a = []
    for i in str(text):
        a.append(i)
        if i in "aeiouAEIOU":
            a.remove(i)
    return ''.join(a)
print anti_vowel("helloworld")
