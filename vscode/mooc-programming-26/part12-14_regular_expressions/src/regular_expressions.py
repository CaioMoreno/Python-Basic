# Write your solution here
import re

def is_dotw(my_string: str):
    return bool(re.search("Mon|Tue|Wed|Thu|Fri|Sat|Sun", my_string))

def all_vowels(my_string: str):
    return bool(re.search("^[aeiou]*$", my_string))

def time_of_day(my_string: str):
    return bool(re.search("^([0-1][0-9]|[0-2][0-3])+:+([0-5][0-9])+:+([0-5][0-9])$", my_string))

