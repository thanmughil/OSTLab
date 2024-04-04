class InvalidAge(Exception):
    def __init__(self, message="Age Below 18!"):
        self.message = message
        super().__init__(self.message)

age = int(input("Enter the age : "))

try:
    if age < 18:
        raise InvalidAge
    else:
        print(age,"is a valid age!")
except InvalidAge:
    print("Enter age above or equal 18!")