from words import words
minionese_to_english = {v: k for k, v in words.items()}


def translate(sentence, minionese=False):
    dictionary = words if not minionese else minionese_to_english

    result = ""
    for word in sentence.split(" "):
        if word in dictionary.keys():
            result += dictionary[word] + " "
        else:
            result += word + " "

    return result[:-1]