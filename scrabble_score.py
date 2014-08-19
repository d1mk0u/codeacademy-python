# slovarj s alfavitom i cifroi
score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
# Nazna4aem funkciju
def scrabble_score(word):
# vse stroki avtomati4eski umenshajutsja
    word = word.lower()
# sozdaem zna4enie total i prisvaevaem 0
    total = 0
#proxodimsja po vxodjashei stroke i vyvodim vse bukvy.
    for x in word:
        x in score
        total += score[x]
    return total
print scrabble_score("PIE")
