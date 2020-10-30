# Python File Operation
# The following operation can be perform on a file using python.
# Read, Write, Update and



# Write to a file
# When writing to a file, you must consider the mode and encoding format
# The mode must be in any of this mode "w,r,x", to show that it is in writing mode while "r+b" means read and write in binary mode(i.e when dealing with images)
# The previous lesson that shows how to read from a file has the default closing format but there is a 
# safer way to do this using either the "try---finally" exception handling or the "with" keyword. 


# Add a new student to the list
# this operation will create a new file if the file does not exist.
# if the file exist, it will overwrite all its content with the newly added one.

#try:
#    list = open("student-new-list.txt", mode="w", encoding='utf-8')
#    list.write("\n11. Goliath Juel")
#finally:
#    list.close()

# A safer way of closing a written file using the "with" keyword.
with open('student-new-list.txt', mode='w', encoding='utf-8') as list:
    list.write("NEWLY ADMITTED STUDENTS\n")
    list.write("\nGoliath Juel")
    list.write("\nNathanel Ijeoma")
    list.write("\nOkeke Paul")
    list.write("\nMadueke Gloria")
    list.write("\nAsena Princess")
    list.write("\n\nThe above name has just been added to this file.")


# using the append mode to add data to a file
with open('student-new-list.txt', mode='a', encoding='utf-8') as list:
    list.write("\n\nAPPENDED STUDENTS\n")
    list.write("\nChima ajuchachi")
    list.write("\nUdeze gloria")
    list.write("\nNduka Mariam")
    list.write("\nNduka Charlse")
    list.write("\nAsena Princess")
