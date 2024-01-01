# Creating a variable with the phrase.
phrase = "Hello World"
# Creating an empty variable for a modified phrase.
new_phrase = ""

# Create a for loop to iterate over the length of the variable 'phrase', reflecting the index number of the variable.
for i in range(len(phrase)):
    # To change the case of the letters in a phrase, I check that dividing the index number returns 0, this way I can
    # change the first and every second letter in the phrase to upper case.
    if i % 2 == 0:
        new_phrase += phrase[i].upper()
    else:
        new_phrase += phrase[i].lower()

# Displaying the transformed phrase.
print(new_phrase)
