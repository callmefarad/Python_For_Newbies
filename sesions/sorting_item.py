# SORT
# the sorted() function is used to sort items in ascending order by default or by user prescriptions.
# basic sorting is used without a key and mapping function

# BASIC SORT
# sorting items in a list
print('\nsorted() function shows all the items in ascending order')
items = [1, 29, 37, 97, 2, 57, 37, 58, 46, 61, 74, 9273, 54]
print(sorted(items))

# Enumerator helps us know the index of we would like to sort
print('\nEnumerator helps us to know the index number of itme we would want to sort for.')
print(list(enumerate(items)))

# we can also impose a start index value rather than the default (0)
print('Making the index to start with 1 rather than the default(0) value.')
print(list(enumerate(items, start=1)))


# KEY FUNCTION SORT
# sorting items using the keyword "sorted", "key function" and "mapping funtion".
# it takes this format: sorted(object list, key=lambda: class_name: class.name(where class.name is the property to sort))
# (sorted(list of objects, key=lambda, maping the class to the property in the argument to sort))
class Student:
    # create an init function that serve as the construct of the class
    def __init__(self, name, age, python_score, django_score, ml_score):
        # defining the propertis contained in the class
        self.name = name
        self.age = age
        self.python_score = python_score
        self.django_score = django_score
        self.ml_score = ml_score

    # __repr__() function return a string containing a printable representation of an object.
    def __repr__(self):
        return repr((self.name, self.age, self.python_score, self.django_score, self.ml_score))


# creating instances of the Student class
nd = Student("ndidi", "45", "100", "100", "100")
ol = Student('ola', '75', '150', '200', '250')
tb = Student('tobi', '20', '200', '175', '150')
om = Student('oma', '30', '100', '100', '100')

# putting the created objects in a list
object_list = [
    nd, ol, tb, om
]

# sorting the objects by age
print("\nsorting the objects by age:")
sorted_items = sorted(object_list, key=lambda Student: Student.age)
print(sorted_items, '\n')

# sorting the objects by python score
print("sorting the objects by python score:")
sorted_items = sorted(object_list, key=lambda Student: Student.python_score)
print(sorted_items, '\n')

# sorting the objects by django score
print("sorting the objects by django score:")
sorted_items = sorted(object_list, key=lambda Student: Student.django_score)
print(sorted_items, '\n')

# sorting the objects by ml score
print("sorting the objects by machine learning score:")
sorted_items = sorted(object_list, key=lambda Student: Student.ml_score)
print(sorted_items, '\n')


# we can also use the same method to sort for tupple
class_list = [
    ("charles", 45, "100", "100", "1"),
    ('hammed', 75, '150', '200', '250'),
    ('kingsley', 20, '200', '175', '150'),
    ('james', 30, '100', '100', '100'),
]

# sorting the class list by age
print('sorting the ages of students in tupple (student_list).')
sorted_list = sorted(class_list, key=lambda Student: Student[1])
print(sorted_list)


# OPERATOR MODULE FUNCTION
# The key-function patterns shown above are very common, so Python provides convenience functions to make
# accessor functions easier and faster. The operator module has itemgetter(), attrgetter(), and a 
# methodcaller() function.

# itemgetter() function look at the index to find element while the attrgetter() function look at the name(string) of the name of 
# the passed in the agument.
# the itemgetter() function is used for tupple while the attrgetter() function is used for list
# we must first import the itemgetter() and attrigetter() function from the operator module

from operator import itemgetter, attrgetter

print('using itemgetter() function to dislplay students age of object in Student class(tupple)')
print(sorted(class_list, key=itemgetter(1)))
print('')
print('using attrgetter() function to display students age of object in Student class (list)')
print(sorted(object_list, key=attrgetter('age')))


# DESCENDIGN SORT
# Both list.sort() and sorted() accept a reverse parameter with a boolean value. This is used to flag descending 
# sorts. For example, to get the student data in reverse age order:

# sort students in descending order
print('\nthe reverse order of student age:')
sorted_list = sorted(object_list, key=attrgetter('age'), reverse=True)
print(sorted_list)


# the min() function checks for the minimum value while the max() checks for the maximum value in a list, tuple or dictionary
print('\nDisplay the student who got the highest score in python')
maximum_no = max(object_list, key=attrgetter('python_score'))
print(maximum_no)

print('\nDisplay the student who got the highest score in django')
maximum_no = max(object_list, key=attrgetter('django_score'))
print(maximum_no)

print('\nDisplay the student who got the highest score in machine learning')
maximum_no = max(object_list, key=attrgetter('ml_score'))
print(maximum_no)

print('\nDisplay the student who got the lowest score in python')
minimum_no = min(object_list, key=attrgetter('python_score'))
print(minimum_no)

print('\nDisplay the student who got the lowest score in django')
minimum_no = min(object_list, key=attrgetter('django_score'))
print(minimum_no)

print('\nDisplay the student who got the lowest score in machine learning')
minimum_no = min(object_list, key=attrgetter('ml_score'))
print(minimum_no)



