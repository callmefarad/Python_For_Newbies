# Grid list is a kind of nested list


#grid list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

# displaying each list in the gride list
for row in number_grid:
    for col in row:
        print(col, end='')
print('\n'*2)
