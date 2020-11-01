from prettytable import PrettyTable

# creating a class for the application
class Exam:
    """ DOCUMENTATION: Exam class takes 2 arguments: (question(String), answer(String)). """
    # construct of the class
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer



# create a function to run the application
def run_app(question_list):
    """ DOCUMENTATION: run_app() functions takes 1 argument. (question_list(String)) """
    # Ask the user to prompt his/her name
    name = input("What is your name? ")
    score = 0
    for i in question_list:
        userinput = input(i.question)
        if userinput == i.answer:
            score += 1
    if score < 3:
        remark = "Failed"
    elif score > 3 and score < 5:
        remark = "Passed"
    else:
        remark = "Excellent"

    # store the estimated value of score to a variable named result
    result = score
    # total questions
    total = len(question_list)
    #creating an instance of class prettyTable()
    x = PrettyTable()
    # creating the fields i.e columns of the table
    x.field_names = ['Names', 'Score', 'Total Score', 'Remark']
    # add values to the table fields created
    x.add_row([name, result, total, remark])
    # print all record in a tabular format
    print(x)
    print("\n")
    print("Name: ", name, "\nScore: ", score, "\nTotal Score: ", len(question_list), "\nRemark: ", remark)


