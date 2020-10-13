# ----------------------------------try except exception handling--------------------------



print("Enter num 1")
num1 = input()
print("Enter num 2")
num2 = input()
# print("The sum of these two number is",
# int(num1)+ int(num2))
try:
    print("The sum of these two number is",
int(num1)+ int(num2))
    
except Exception as e:
    print(e)

print("this is line is very important")
# try except exception is use to get the no error in the terminal if you put num1=er then you will see
