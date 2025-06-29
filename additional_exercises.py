f = open('words_copy.txt')
text = f.read()
realtext = text.split()

def uses_any(word):
    for letter in word:
        if letter in 'spadclrk':
            return False
    return True


def wordle():
    for word in realtext:
        if len(word) == 5 and 'e' in word and uses_any(word) and not word[4] == 'e' and not word[2] == 'e':
            print(word)

wordle()