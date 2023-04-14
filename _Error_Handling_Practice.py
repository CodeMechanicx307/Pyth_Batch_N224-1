num1=int(input())
num2=int(input())
try:
 div= num1 /num2
except Exception  :
  print("Error:Zero divison error")
else:
    print(div)
finally:
    print("Always")
print("Done!")
