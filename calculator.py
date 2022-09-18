firstNumber = int(input("Enter your first number: "))
operation = input("Enter your operation (A/S/M/D): ")
validList = ["A", "S", "M", "D"]

while operation not in validList:
    operation = input("Please enter A, S, M, or D: ")

secondNumber = int(input("Enter your second number: "))

if operation == "A":
    result = firstNumber + secondNumber
    print("The result is " + str(result))
elif operation == "S":
    result = firstNumber - secondNumber
    print("The result is " + str(result))
elif operation == "M":
    result = firstNumber * secondNumber
    print("The result is " + str(result))
else:
    result = firstNumber/secondNumber
    print("The result is " + str(result))
