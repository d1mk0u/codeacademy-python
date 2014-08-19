def censor(text, word):
    return text.replace(word, "*" * len(word))
print censor("What the heck", "heck")
