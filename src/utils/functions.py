import sys
from random import randint, choice
from time import sleep


def join_script_arguments():
    sys.argv.pop(0)
    return "".join(sys.argv)


def get_file_content(file_path):
    f = open(file_path, "r")
    if f.mode == "r":
        return f.read()


def choose_random_value(mylist):
    return mylist.pop(randint(0,len(mylist)-2))

def overwriter_string(string):
    return "\r{}".format(string)


def overwrite_print(string):
    print(overwriter_string(string), end="")

def question():
	myquestion = ["¿Todo bien ", "¿Como andas ", "¿Que contas ", "¿Que haces ", "¿Como va todo ", "¿En que andas ", "¿Que onda ", "¿Todo tranquilo "]
	return choice(myquestion)
