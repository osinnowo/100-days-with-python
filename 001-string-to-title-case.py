from typing import List

# Using list comprehension approach
def convert_to_title_case_using_list_comprehension(string: str) -> str:
    # Using list comprehension method
    return " ".join([x[0].upper() + x[1:].lower() if x else '' for x in string.split(" ")])


# Using brute-force approach
def convert_to_title_case_using_brute_force_approach(string: str) -> str:
    words = string.split(" ")
    for i in range(0, len(words)):
        words[i] = words[i][0].upper() + words[i][1:].lower()
    else:
        return " ".join(words)
    

# Testing
print(convert_to_title_case_using_list_comprehension(string="hello world! welcome to python programming language"))
print(convert_to_title_case_using_brute_force_approach(string="hello world! welcome to python programming language"))