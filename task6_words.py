

def get_words(line):
    return [*filter(bool, map(str.strip, line.split(",")))]


def get_word_set():
    return set(get_words(input("Write words: ")))


def create_dict(word_set):
    if len(word_set) > 0:
        values = get_words(input("Write %i words: " % len(word_set)))

        result = {}
        for i, w in enumerate(word_set):
            result[w] = values[i]

        return result
    return None


word_set = get_word_set()
print(word_set, len(word_set))
print(create_dict(word_set))
