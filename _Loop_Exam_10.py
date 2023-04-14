
def finddifference (Bangladeshi_soilder,Indian_soilder):
    return (Bangladeshi_soilder - Indian_soilder)

Bangladeshi_soilder = float(input("Enter the first number: "))
Indian_soilder = float(input("Enter the second number: "))

for start in range(0,1):
    difference = finddifference(Bangladeshi_soilder,Indian_soilder)
    print(" DIFFERENCE #{} : {} ".format(start+1,difference))

"""
times = int(input("Enter the number of times to calculate the difference: "))
num = []
lst = list(value for value in range (1,232))
for start in range (0,232):
    if num not in lst :
        lst.append(num)
print(num)
"""
"""
print("My_list",lst)
real_num = set(lst)
print(lst)

"""