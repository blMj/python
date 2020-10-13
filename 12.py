# recursive and recursion



def factorial_iterative(n):
    """
       :param n:Integer
       :return: n* n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(n):
        fac=fac*(i+1)
    return fac

# factorial_iterative(5)
print(factorial_iterative(5))
def factorial_recursion(n):
    """
       :param n:Integer
       :return: n* n-1 * n-2 * n-3.......1
    """
    if n==1:
        return 1
    else:
        return n * factorial_recursion(n-1)
    # 5*4
    # 4*3
    # 3*2
    # 2*1
print(factorial_recursion(5))

# 0 1 1 2 3 5 8 13
# 0+1=1;1+1=2;1+2=3;2+3=5.......
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


number=int(input("Enter your number"))
# print("factorial using iterative method" ,factoria;_iterative(number) )
# print("factorial using recursion method" ,factoria;_recursion(number) )
print(fibonacci(number))
