# This progrma is called the cow translation language.
# It converts every vowel letter found in a word to "COW", thereby forming the cow language.


# defining the function
def copywrite():
    print("Copywrite: Ubani U. Friday")


def translate(phrase):
    word_translation = ""  # an empty variable to hold each element of any work inputed
    for letter in phrase:
        if letter in "AEIOUaeiou":
            word_translation = word_translation + "cw"
        else:
            word_translation = word_translation + letter
    return word_translation


# main program
userinput = input("\nEnter any word or sentence you like to translate to a cow language: ")
print(translate(userinput))
copywrite()
