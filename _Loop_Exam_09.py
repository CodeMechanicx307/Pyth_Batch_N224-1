t = int(input("Enter the numbers:-"))   # read the number of test cases

for start in range(t):
    a, b = map(int,input().split())  # read the two integers
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
"""
In this code ,At first i had taken input from the user and i gave a condition that the input must be an integer
.After that, i had taken a for loop which continuous it,s iteration from t.After that, i had taken a and b
two variables in a combine pack (for giving number one per line).Then i,used map function which,s structure is
(function,iterable) it takes all existing value in code .Then i, used split and used if,else,elif condition.
After doing that,i gave run command .  

"""
