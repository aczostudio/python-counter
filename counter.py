import json

class programming_lang:
    def __init__(self, lname):
        self.lang_name =""
        self.score = 0

lang_array =[]

print("Choosing counter options")
print("1.adding language")
print("2.voting language")
options = input("Please input options\n")
if(options == "1"):
    input_lang_name = input("Please programming language name\n")
    programming_lang(input_lang_name)
    lang_array.append(programming_lang)