# decorators




# def funtion_1():
#     print("let's go ")
# fun2 = funtion_1
# del funtion_1
# fun2()





# def funcshow(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum
# a = funcshow(1)
# print(a)
# a = funcshow(0)
# print(a)




# def executor(func):
#     func("hello")
# executor(print)




def dec1(func1):
    def nowexe():
        print("executing now")
        func1()
        print("executed")
    return nowexe
@dec1
def who_are_you():
    print("I am a coder")
# who_are_you = dec1(woh_are_you) and @dec1 is same

who_are_you()