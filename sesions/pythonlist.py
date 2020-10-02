# creating a python list
fruits = ['mango', 'pepper', 'orange', 'banana', 'coconut', 'grape']
# display the items in the list
print(fruits)
# display the datatype of the variable fruits
print(type(fruits))

# displays the second item in the list using positive indexing
print('positive indexing', fruits[1])
# display the last item in the list using negative indexing
print('Negative indexing', fruits[-1])

# getting the range of item say "pepper and orange" from the list using positive indexing
print('positive items', fruits[1:3])

# getting the range of item say 'pepper', 'orange', 'banana', 'coconut' from the list using negative indexing
print('negative items', fruits[-5:-1])
# getting the range of items say from "orange to the end of the list" using negative indexing
print('negative items', fruits[-4:])
# displays the item from the third position to the end of the list because the specified end index is beyond the list
print(fruits[3:10])

# creating a check variable
codelab = "grape"

"""
Using the keyword 'in' to perform operation in a list
"""
# checks if the value of codelab is present in the list by using the keyword 'in'
print(codelab in fruits)
# displays the length of the list
print(len(fruits))

""""
my_list = fruits[-5:-1]
print(codelab in my_list)
print(len(my_list))
"""
#fruits = ['mango', 'pepper', 'orange', 'banana', 'coconut', 'grape']
# assigning the range of value to my_list
my_list = fruits[-6:-4]
# gets the length of the new list
stick_length = len(my_list)
# declare new variables
y = 2
z = 3
# performs and arithmetic operation on the variables and assign it to a new variable 'a'
a = y**z

# gets the new length and assigning it to a new variable 'new'
new = stick_length - a
# multiply the result by 2 and display the result
print(new * 2)

"""
Using the append() function to add item to a list
fruits = ['mango', 'pepper', 'orange', 'banana', 'coconut', 'grape']
"""
fruits = ['mango', 'pepper', 'orange', 'banana', 'coconut', 'grape']
new_fruit = "sherry"
fruits.append("pawpaw")
print(fruits)

fruits.insert(3, new_fruit)
print(fruits)

fruits.pop()
print(fruits)

fruits.pop(5)
print(fruits)

sentence = ["i am a boy going to school", "i am a girl going to school.", "ade is a boy."]
sentence.pop(2)
print(sentence)

# using the del keyword
del sentence[1]
print(sentence)

sentence.clear()
print(sentence)
