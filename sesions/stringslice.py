# slicing simply means returning a range of character
# this is done by using indexing pattern
# note when dealing with range the last number is exclusive.
# i.e if we are to get the last letter of digit 10, we would have a
# range of number tending to 11 where the 11th index is exclusive


# declaring my variable
my_string = "This is my string."

# printing the whole value of the variable
print(my_string[:])

# printing the word "my" from the value
print("Am printing the word \"my\" from the variable using string slicing")
print(my_string[8:10])

# we also use negative indexing during slicing
# lets print the word "string" from the back using negative indexing
print("printing the word \"string\" using negative indexing.")
print(my_string[-7:-1])