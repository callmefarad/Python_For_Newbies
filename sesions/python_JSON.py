# JSON is a syntax for storing and exchanging data
# JSON is a text written with JavaScript object notation

# JSON in Python: python has a built in package called json, which can be used to work with JSON data. 
# Before you can use JSON in python, you must first import the module. 
# Convert JSON to Python.
# the json code must be a single quote if it is a single String OR in a triple quote if it is a multiple String.
# single quote: json_code = '{"name":"ubani","age":20,"python_score":87,"django_score":56,"ml_score":90}'
# tripple quote: 
# json_code = '''{
#    "name":"ubani",
#    "age":20,
#    "python_score":87,
#    "django_score":56,
#    "ml_score":90
#}'''


import json

# JSON code
json_code = '''{
    "name":"ubani",
    "age":20,
    "python_score":87,
    "django_score":56,
    "ml_score":90
}'''

# calling the function "loads()" in json module
to_python_code = json.loads(json_code)
# the result is a python dictionary:
print('\n',to_python_code['name'])
print(to_python_code)


# CONVERT FROM PYTHON TO JSON
# python object can be coverted to json by calling the dumps() function from json module

# creating a python dictionary
python_code = {
    "name": "ubani",
    "age": 20,
    "python_score": 87,
    "django_score": 56,
    "ml_score": 90
}

# convet to JSON
to_json_code = json.dumps(python_code)
# the result is a JSON string:
print(to_json_code, '\n')

# The following python types can be converted to JSON strings: 
# dict 
# list 
# tuple 
# string 
# int 
# float 
# True
# False 
# None

print(json.dumps({"name": "ubani", "age": 20, "python_score": 87, "django_score": 56, "ml_score": 90}))
print(json.dumps(['ubani', 20, 34, 87, 89]))
print(json.dumps(('ubani', 20, 83, 34, 58,)))
print(json.dumps('ubani'))
print(json.dumps(56))
print(json.dumps(94.33))
print(json.dumps(True))
print((json.dumps(False)))
print(json.dumps(None))
print('\n')


# Result Format: we can fomat the result of the JSON code to look more appealing by replacing the seperator default value
# (", ",": ") this means using a comma and a space to seperate each object, and a colon and a space to separate keys from values.
# we can override this default sepatator keywords 'indent' and 'separators'.

# converting a python dictionary to a formatted JSON code
x = {"name": "ubani", "age": 20, "python_score": 87, "django_score": 56, "ml_score": 90}
print(json.dumps(x, indent=4, separators=(". "," = ")))

# display the default format with indentation of 4
x = {"name": "ubani", "age": 20, "python_score": 87, "django_score": 56, "ml_score": 90}
print(json.dumps(x, indent=4))

# SORTING
# we can also sort the result of the JSON code

y = python_code = {
    "name": "ubani",
    "age": 20,
    "married": False,
    "educated": True,
    "pets": None,
    "python_score": 87,
    "django_score": 56,
    "ml_score": 90,
    "cars": [
        {"Model": "BMW 230", "Cost": 4000},
        {"Model": "TOYOTA", "Cost": 8000}
    ] 
}

# show a formated JSON result
print(json.dumps(python_code, indent=4))