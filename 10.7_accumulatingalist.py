def is_reverse(word):
    return word == word[::-1]

def is_palindrome(word):
    return word == word[::-1]

word_list = open('words_copy.txt').read().splitlines()

word_dict = {}
for word in word_list:
    word_dict[word] = 1

palindromes = []
for word in word_dict:
    if is_palindrome(word):
        palindromes.append(word)

# print(palindromes[:10])

long_palindromes = []

for word in palindromes:
    if len(word) >= 7:
        long_palindromes.append(word)

# print(long_palindromes[:10])