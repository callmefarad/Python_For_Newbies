# How to delete from a file
# Open the file for reading and use file.readlines() to create a list where each element is a line from the file. 
# Use the syntax del list[index] with list as the list of lines to delete the element at index. 
# Write the edited list of lines to a file to create a new file without the deleted line.


# Deleting from a file
# Opening a file for reading
with open('student-deleted-list.txt', mode='r', encoding='utf-8') as list:
  lines = list.readlines()

# Delete line 1
del lines[1]

# Open the file as a new file and write the remaining line to it.
with open('student-deleted-list.txt', mode='w', encoding='utf-8') as new_list:
    for line in lines:
        new_list.write(line)


