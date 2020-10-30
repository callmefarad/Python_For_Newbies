# Recursive function is a function that call itself.
# Recursion is used to breakdown complex problems to smaller problems.
# There are algorithms that uses the process of recursion.


# write a program that performs a permutation of numbers using recursive function
# defining functions
def permutation(n):
    if n > 1:
        return n * permutation(n-1)
    else:
        return 1


# A recursive function that check if any word or sentence is alphabetically arranged
def is_alphabetical_order(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_alphabetical_recursive(word[1:])



# A normal function that check if any word or sentence is alphabetically arranged
def is_alphabetical_normal(word):
	i = 0
	while i < len(word)-1:
		if word[i+1] < word[i]:
			return False
		i = i+1
	return True

def is_alphabetical_normal2a(word):
	i = 0
	while i < len(word)-1:
		if word[i] > word[i+1]:
			return False
		i = i+1
	return True

# the main program
# where n = 16
userinput = input("Enter the number you want to permutate: ", )
print("The permutation of", userinput, "is: ", permutation(int(userinput)))

userinput = input("Enter a word to check if the letters are in alphabetic order: ")
print(is_alphabetical_recursive(userinput))

userinput = input("Enter a word to check if the letters are in alphabetic order: ")
print(is_alphabetical_normal(userinput))

userinput = input("Enter a word to check if the letters are in alphabetic order: ")
print(is_alphabetical_normal2a(userinput))