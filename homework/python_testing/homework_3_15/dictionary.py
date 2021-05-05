dictionary = {}


def add_word(word, paras):
    dictionary[word] = paras
    return dictionary[word]


def del_word(word):
    if word in dictionary:
        del dictionary[word]
        return True
    else:
        return False


def get_word(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return None


def revise_word(old, new):
    if old in dictionary:
        temp = dictionary[old]
        del dictionary[old]
        dictionary[new] = temp
        return True
    else:
        return False


def add_paras(word, paras):
    if word in dictionary:
        dictionary[word] += paras
        return dictionary[word]
    else:
        dictionary[word] = paras
        return dictionary[word]
