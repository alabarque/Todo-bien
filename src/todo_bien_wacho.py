import sys
from os.path import dirname, abspath
from utils.functions import join_script_arguments, get_file_content, overwriter_string, overwrite_print, choose_random_value, question


# Script arguments validator
#if len(sys.argv) == 1:
#    print("Si?")
#    user_input = input()
#else:
sys.argv
user_input = join_script_arguments()

# Read file and turn content to list
content = get_file_content(abspath(dirname(__file__)) + "/../resources/replies")

replies = content.split("\n")

# Choose replies
for x in range(5):
	print(overwriter_string(question() + choose_random_value(replies) + "?"))

