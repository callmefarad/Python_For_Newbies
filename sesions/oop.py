
# create a class with name "student".
# create an __init() function of the class.
# create 4 objects of the class.
# get the lowest python score of the objects created.
# get the highest machine learning score of the object created.
# create an object method that gives the sum of all the scores of the object created.
# Assignment display in the objects in ascending order by age.

# OBJECT METHOD
# an object method is a function in the object class



# step 1
# creating a class
class student:
    # step 2
    # creating an __init__() function
    def __init__(self, name, age, python_score, django_score, ml_score):
        self.name = name
        self.age = age
        self.python_score = python_score
        self.django_score = django_score
        self.ml_score = ml_score

     # __repr__() function return a string containing a printable representation of an object.
    def __repr__(self):
        return repr((self.name, self.age, self.python_score, self.django_score, self.ml_score))

    # creating an object method
    def sum(self):
        result = self.python_score + self.django_score + self.ml_score
        return result


# creating a child class
class Promotion(student):
    def __init__(self, level, courses, incentive):
        self.level = level
        self.incentive = incentive
        self.courses = courses

    def upgrade(self):
        print("Total Course Taken: ", self.courses, "\nCongratulations Mr. ", x.name,  "\nPromoted to Level: ", self.level, "\nCurrent Benefit: ", self.incentive)




# step 3
# creating 4 instances of the class
tobi = student("micheal", 20, 90, 50, 24)
oma = student("oma", 19, 91, 48, 86)
precious = student("precious", 23, 89, 38, 74)
ola = student("ola", 39, 100, 19, 87)

# creating a list of objects of the class
group_of_students = [
    tobi, oma, precious, ola
]

# step 4
# checks for the student object with the lowest python score 
if tobi.python_score < oma.python_score and tobi.python_score < precious.python_score and tobi.python_score < ola.python_score:
    print("\nlowest python score: ",tobi.python_score, "Name: ", tobi.name)
elif oma.python_score < tobi.python_score and oma.python_score < precious.python_score and oma.python_score < ola.python_score:
    print("\nlowest python score: ",oma.python_score, "Name: ", oma.name)
elif precious.python_score < tobi.python_score and precious.python_score < oma.python_score and precious.python_score < ola.python_score:
    print("\nlowest python score: ",precious.python_score, "Name: ", precious.name)
else:
    print("\nlowest python score: ",ola.python_score, "Name: ", ola.name)


# step 5
# checks for the student object with the highest machine language score
if tobi.ml_score > oma.ml_score and tobi.ml_score > precious.ml_score and tobi.ml_score > oma.ml_score:
    print("\nHighest machine learning score: ",tobi.ml_score, "Name: ", tobi.name)
elif oma.ml_score > tobi.ml_score and oma.ml_score > precious.ml_score and oma.ml_score > ola.ml_score:
    print("\nHighest machine learning score: ",oma.ml_score, "Name: ", oma.name)
elif precious.ml_score > tobi.ml_score and precious.ml_score > oma.ml_score and precious.ml_score > ola.ml_score:
    print("\nHighest machine learning score: ",precious.ml_score, "Name: ", precious.name)
else:
    print("\nHighest machine learning score: ",ola.python_score, "Name: ", ola.name)
print("\n")


# step6
# create an object method that gives the sum of all the scores of the objects created.
print("The sum of python score of", tobi.name, "is: ", tobi.sum())
print("The sum of python score of", ola.name, "is: ", ola.sum())
print("The sum of python score of", oma.name, "is: ", oma.sum())
print("The sum of python score of", precious.name, "is: ", precious.sum())
print('\n')

# step 7
# display the objects in scending order by age
# we will import itemgetter from operator module
# then we def the __repr__() function that helps display the string
from operator import attrgetter

print('The list of students in ascending order by age:')
print(sorted(group_of_students, key=attrgetter('age')))
print("\n")



# INHERITANCE
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from which is also called base class.
# Child class is the class that inherits rom another class which is the derived class.

# creating instance of the class Promotion
x = Promotion(400, 3, "$8,000")
# inheriting the properties of the parent class "student"
x.name = "Collins Edward"
x.python_score = 100
x.django_score = 100
x.ml_score = 100

# inheriting method "sum()" from the parent class
print("Total Score: ", x.sum(),)
# displays to the screen using the method from the child class
print(x.upgrade())

# displace the properties inherited by the child instance from the parent class
print("\nTotal Score: ", x.sum(), "\nTotal Course Taken: ", x.courses, "\nCongratulations Mr. ", x.name,  "\nPromoted to Level: ", x.level, "\nCurrent Benefit: ", x.incentive)
