# working with tuple
# a representation of a tuple
fruits = ('mango', 'grape', 'agbalumo', 'likiki')

# getting the item (mango) in the tuple using indexing
print(fruits[0])

# getting the whole items in the tuple
print('\nThis show the items in the tuple: ', fruits[0:])

print('using a negative indexing to show the list of items in the tuple: ', fruits[-4:])

# using the keyword "in" to check for an item in a list
word = "guava"
print(word in fruits)


gam = ('mango', 'grape', 'agbalumo', 'likiki')
new_gam = list(gam)
# new_gam.append('lakan')
second_list = ['lekan', 'ola', 'john']

print('concatenating the list', new_gam + second_list)

new_gam.extend(second_list)
print('extend', new_gam)
y = ('g', 'o')
z = ('a', 't')

print(y + z)
print(type(y+z))


