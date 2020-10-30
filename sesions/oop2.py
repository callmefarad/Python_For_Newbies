# creating a class
# a class definition can not be empty but if for some reason you don't have any values for the class, pt the keyword "pass" as the statement in the class.

class Student:
    college = "BrighterDays CodeLab"
    # create an init function that serve as the construct of the class
    # to understand the meaning of a class, you must first understand the built-in __init__() function, which is always
    # executed when the class is being initiated.
    # the __init__() function is used to assign values to object properties, or other operaitions that are necessary to do when the object is beign created

    def __init__(self, name, age, python_score, django_score, ml_score):
        # defining the propertis contained in the class
        self.name = name
        self.age = age
        self.python_score = python_score
        self.django_score = django_score
        self.ml_score = ml_score

    # creating a display string function
    def __repr__(self):
        return repr((self.name, self.age, self.python_score, self.django_score, self.ml_score))

    # creating an object method
    # An object method is simply a function that belongs to the object.
    def total_score(self):
        result = self.python_score + self.django_score + self.ml_score
        return result

# main program
# creating an instance of the Student
nd = Student("ndidi", 45, 100, 100, 100)
# getthing the pytthon score of ndidi
print('\nPython score for ndidi: ', nd.python_score, '\n')
# creating another instance of the Student
ol = Student('ola', 75, 150, 200, 250)
# getthing the pytthon score of ola
print('\nPython score for ola: ', ol.python_score, '\n')
# creating another instance of the Student
tb = Student('tobi', 20, 200, 175, 150)
# getthing the pytthon score of tb
print('\nPython score for tb: ', tb.python_score, '\n')
# creating another instance of the Student
om = Student('oma', 30, 100, 100, 100)
# getthing the pytthon score of oma
print('\nPython score for oma: ', om.python_score, '\n')

# an object can also be deleted using the keyword "del"
# del om


# creating a list of the instance
student_list = [
    nd, ol, tb, om
]

# display the ages of all the students 
for student_properties in student_list:
    print(student_properties.age)

# display the global variable of the class
print(Student.college)


# display student with the loweest score in python
print('Method 1:(Student with the lowest score in python is:)''\n')
if nd.python_score < ol.python_score and ol.python_score > tb.python_score and tb.python_score > om.python_score:
    print(nd.name ,nd.python_score)
elif ol.python_score < nd.python_score and nd.python_score > ol.python_score and ol.python_score > om.python_score:
    print(ol.name ,ol.python_score)
elif tb.python_score < nd.python_score and nd.python_score > ol.python_score and ol.python_score > om.python_score:
    print(tb.name ,tb.python_score)
else:
    print(om.name ,om.python_score)

print('Method 2:(Student with the lowest score in python is:)''\n')
if nd.python_score < ol.python_score and nd.python_score < tb.python_score and nd.python_score < om.python_score:
    print(nd.python_score)
elif ol.python_score < nd.python_score and ol.python_score < tb.python_score and ol.python_score < om.python_score:
    print(ol.python_score)
elif tb.python_score < nd.python_score and tb.python_score < ol.python_score and tb.python_score > om.python_score:
    print(tb.python_score)
else:
    print(om.python_score)

# an instance accessing the global variable
print(nd.college)

# display the total score for all the objects using the object method created
print("\nName:",ol.name, "Score:",ol.total_score())
print("\nName:",om.name, "Score:",om.total_score())
print("\nName:",nd.name, "Score:",nd.total_score())
print("\nName:",tb.name, "Score:",tb.total_score())


