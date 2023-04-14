"""
def find_Minimum(num):
    minimum=num[0]
    for start in range(1,len(num)):
        if num[start]<minimum:
            minimum=num[start]
    return minimum
print(find_Minimum([34,56,23,45,78,21,13]))

a=(lambda a,b : a+b) (2,3)
print(a)
"""
"""
while True:

    print("Please select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = getUserInput("Enter choice (1/2/3/4/5): ")

    if choice == '5':
        break

    num1 = getUserInput("Enter first number: ")
    num2 = getUserInput("Enter second number: ")

    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))
    else:
        print("Invalid Result")
"""