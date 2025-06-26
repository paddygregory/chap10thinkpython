def counter(string):
    values = {}
    for letter in string:
        if letter not in values:
            values[letter] = 1
        else:
            values[letter] += 1
    return values

# print(counter('hello world'))

def exc_count(string):
    values = {}
    for letter in string:
        if letter.islower():
            if letter not in values:
                values[letter] = 1
            else:
                values[letter] += 1
    return values

print(exc_count('Hello World!'))
