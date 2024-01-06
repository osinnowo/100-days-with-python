from typing import List, AnyStr

try:
    with open("hello.txt", "r") as file:
        lines: List[AnyStr] = file.readlines()
        for line in lines:
            print(line)
except:
    print("Something went wrong!")