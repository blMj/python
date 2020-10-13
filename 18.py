# map,filterandd reduce




# map is use to apply function in whole list
number=["3","5","6","7","9"]
number=list(map(int,number))
# for i in range(len(number)):
#     number[i]=int(number[i])
number[3] = number[3] +1
print(number[3])


num = [2,4,8,5,68,9,73,99,80]
# def squ(a):
#     return a*a
# square=list(map(squ,num))
# square=list(map(lambda x:x*x,num))
# print(square)

def square(a):
    return a*a

def cube(a):
    return a*a*a
func=[square,cube]
# notice the length is given 0,1,2,3,4,5,6,7,8 in num
for i in range(len(num)):
    val = list(map(lambda x:x(i),func))
    print(val)


# filter
# give the true value
def greater_5(numb):
    return numb>=5
greater__5 = list(filter(greater_5,num))
print(greater__5)


# reduce
from functools import reduce

list1=[2,4,3,5,6]
# num=0
# for i in list1:
#     num=num+i
# you can multiply 
num=reduce(lambda x,y :x+y , list1)
print(num)