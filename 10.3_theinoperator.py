word_list = open('words_copy.txt').read().split()

def word_dict():
    word_dict = {}
for word in word_list:
    word_dict[word] = 1

def reverse_word(word):
    return ' '.join(reversed(word))

def faster():
    count = 0
    for word in word_dict:
        if reverse_word(word) in word_dict:
            count += 1
    return count

print(faster())

