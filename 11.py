# scope,global variables and global keyword 




# Global variable are
a = 6
m = 5
l = 3
def fun_1(n):
    """this is the local variable"""
    global l
    m=4
    l=6
    l=l+65
    print(l,m)
    print(n,"I have printed")
fun_1("this is me")
# print(l) here terminal excute that l =3 but we define l=6
# the function will find the vaule of l is in the list or not function find outside the funtion any variable is there is not then it will give error
# if we want to change the global value ,we have to use global keyword with that variable 




