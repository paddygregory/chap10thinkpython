words = ['apple', 'banana', 'cherry', 'banana']

word_set = set(words)

query = 'banana'

if query in word_set:
    #print(f"{query} is in the set.")
    pass
else:
    #print(f" the set does not contain {query}.")
    pass

# print(query in word_set)

# EX ONE
def value_counts(word):
    value = {}
    for letter in word:
        value[letter] = value.get(letter, 0) + 1
    return value

        

#print(value_counts('brontosaurus'))
# EX TWO
def has_duplicates(word):
    value = {}
    for letter in word:
        value[letter] = value.get(letter, 0) + 1
        if 1 < value.get(letter,0):
            return False
    return True

# print(has_duplicates('brzs'))

# EX FOUR- find repeats

repeats = {'apple' : 2, 'banana': 2, 'cherry': 1}

def find_repeats(counter):
    result = []
    for key in counter:
        if counter[key] > 1:
            result.append(key)
    return result

# print(find_repeats(repeats))

# EX FIVE - add counters

d1 = {'apple': 2, 'banana': 1}
d2 = {'banana': 2, 'cherry': 1}

def add_counters(d1,d2):
    result = d1.copy()
    for key, value in d2.items():
        if key in result:
            result[key] += value
        else:
            result[key] = value
    return result

 
# print(add_counters(d1, d2))

# EX SIX - values above ten
        
hello = {'a': 1, 'b': 2, 'c': 3, 'd': 11, 'e': 12}

def values_above_ten(counter):
    result = []
    for key in counter:
        if counter[key] > 10:
            result.append(key)
    return result

# print(values_above_ten(hello))

# EX SEVEN - interlocking

f = open('words_copy.txt')
text = f.read()
realtext = text.split()

def interlocking(word):
    return word[0::2] in realtext and word[1::2] in realtext
    
print(interlocking('schooled'))

#print(interlocking('school'))