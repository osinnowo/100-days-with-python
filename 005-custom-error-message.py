class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    message: str

    def __init__(self, message: str):
        self.message = message

    def __str__(self):
        return self.message


def validate():
    age = int(input("Welcome to Python's club. Please enter your age:"))
    if age <= 17:
        raise InvalidAgeException(message=f"Invalid age {age}! Please try again")
    else:
        return "Welcome"


try:
    output = validate()
    print(output)
except InvalidAgeException as error:
    print(error)
