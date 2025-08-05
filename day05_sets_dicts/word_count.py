text = "the dog barks and the dog runs"
def word_count(string):
    string_array = string.split(' ')
    d = {}

    for i in string_array:
        d[i] = string.lower().count(i)

    print(d)
    return d

word_count(text)
