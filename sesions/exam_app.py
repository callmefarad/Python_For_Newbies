# importing the class and function from exam_mod
from exam_mod import Exam, run_app

# creating a list of questions 
question_list = [
    "(1)    whats the name of your python instructor?\n(a) ubani\n(b) peter\n(c) bukola\n\n",
    "(2)    an application on a tablet is known as _____?\n(a) web app\n(b) mobile app\n(c) desktop app\n\n",
    "(3)    sum is used to subtract values.\n(a) True\n(b) None\n(c) False\n\n",
    "(4)    django is a ____?\n(a) programming language\n(b) framework\n(c) IDE\n\n",
    "(5)    ____ is used to access the value in dictionary?\n(a) key\n(b) id\n(c) class\n\n",
]


# creating a list (question) of instances of the class "Exam" in the exam.mod
question = [
    Exam(question_list[0], 'a'),
    Exam(question_list[1], 'b'),
    Exam(question_list[2], 'c'),
    Exam(question_list[3], 'b'),
    Exam(question_list[4], 'a'),
]

# main program
run_app(question)

