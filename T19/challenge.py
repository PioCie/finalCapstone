# 1. Add a prefix to a word

def add_prefix_un(word):
    print("un" + word)


add_prefix_un("happy")
add_prefix_un("manageable")


# 2. Add prefixes to word groups


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    words = vocab_words[1:]

    # Apply the prefix to each word in the list
    prefixed_words = [prefix + word for word in words]

    # Combine the prefix and prefixed words into a string
    result = ' :: '.join([prefix] + prefixed_words)

    print(result)


make_word_groups(['en', 'close', 'joy', 'lighten'])
make_word_groups(['pre', 'serve', 'dispose', 'position'])
make_word_groups(['auto', 'didactic', 'graph', 'mate'])
make_word_groups(['inter', 'twine', 'connected', 'dependent'])


# 3. Remove a suffix from a word

def remove_suffix_ness(word):
    # Removed suffix from word
    word_without_suffix = word[:len(word) - 4]
    if word_without_suffix[len(word) - 5] == "i":
        # Reverses the string and replaces the first occurrence of a letter "i" with "y" and reverts the string back to
        # its original order
        basic_word = word_without_suffix[::-1].replace("i", "y", 1)[::-1]
        print(basic_word)
    else:
        print(word_without_suffix)


remove_suffix_ness("heaviness")
remove_suffix_ness("sadness")

# 4. Extract and transform a word


def adjective_to_verb(sentence, index):
    # Split the sentence into a list of words
    words = sentence.split()

    # Get the adjective at the specified index
    adjective = words[index].strip('.,?!')

    verb = adjective + 'en'
    print(verb)


adjective_to_verb('I need to make that bright.', -1)
adjective_to_verb('It got dark as the sun set.', 2)



