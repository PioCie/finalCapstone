# Creating a variable with the phrase.
phrase = "Hello World"
# Creating an empty variable for a modified phrase.
new_phrase = ""

# I create a for loop to iterate over the length of the variable 'phrase', reflecting the index number of the variable.
for i in range(len(phrase)):
    # To change the case of the letters in a phrase, I check that dividing the index number by 2 returns 0,
    # this way I can change the first and every second letter in the phrase to upper case.
    if i % 2 == 0:
        new_phrase += phrase[i].upper()
    else:
        new_phrase += phrase[i].lower()

# Displaying the transformed phrase.
print(new_phrase)

########################################################################################################################

# Creating a variable with the sentence.
sentence = "I am learning to code"
# Using the 'split' method, I split the sentence into individual words, from which I create an iterable list.
split_sentence = sentence.split(" ")
# Creating an empty list of words for changed words
list_of_words = []
# I create a for loop to iterate over the length of the 'split_sentence' list, the index number reflects each word in
# the list.
for i in range(len(split_sentence)):
    # To change the case of the words in a sentence, I check that dividing the index number by 2 returns 0,
    # this way I can change the first and every second word in list to lower case.
    if i % 2 == 0:
        # If the condition is met, adds the changed word to the word list
        list_of_words.append(split_sentence[i].lower())
    else:
        list_of_words.append(split_sentence[i].upper())
# Takes a list of strings and joins them with '" "' to create a sentence.
new_sentence = " ".join(list_of_words)
# Displaying the transformed sentence.
print(new_sentence)
