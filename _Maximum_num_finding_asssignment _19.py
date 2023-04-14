"""
def find_Maximum(num):
    maximum=num[0]
    for start in range(1,len(num)):
        if num[start]>maximum:
            maximum=num[start]
    return maximum
print(find_Maximum([34,56,23,45,78,21,13]))
"""
import math
def Add (number1, number2):
    return number1 + number2

def Sub (number1, number2):
    return number1 - number2

def Mul (number1, number2):
    return number1 * number2

def rem (number1, number2):
    return number1 / number2

def Per (number1, number2):
    return number1 % number2

def Square (number1):
    return number1**2

def Cube (number2):
    return number2**3

def Root (number1):
    return math.sqrt(number1)

def Fact (number2):
    return math.factorial(number2)

def Log (number1):
    return math.log(number1)

def Sin (number1):
    return math.sin(number1)

def Cos (number1):
    return math.cos(number1)

def Tan (number1):
    return math.tan(number1)


a= float(input())
b= float(input())
c= int(input())
d= math.pi/(int(input()))

result= Add(a, b), Sub(a, b), Mul(a, b), rem(a, b), Per(a, b), Square(a), Cube(b), Root(a), \
    Fact(c), Log(c), Sin(d), Cos(d), Tan(d)
print(result)
