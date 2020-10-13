# anonymous and lambda function




# Function declaration is as follows
def fun_1(a,b):
    return a+b
print(fun_1(2,4))

#In lambda or anonymous function
plus = lambda x,y:x+y
print(plus(2,4))

minus = lambda x,y:x-y
print(minus(2,4))


# for sort
a = [[2,86],[2,45],[0,4]]
a.sort(key=lambda x:x[1])
print(a)
# list.sort(kye=myfun, reverse=True|False)