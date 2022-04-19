

def get_words(line):
    return [*filter(bool, map(str.strip, line.split(",")))]


words = set(get_words(input("Write words: ")))
print(words, len(words))

if len(words) > 0:
    values = get_words(input("Write %i words: " % len(words)))

    result = {}
    for i, w in enumerate(words):
        result[w] = values[i]

    print(result)
