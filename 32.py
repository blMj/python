//super and overriding
//overriding=means we are making some class 
and inherit both of them .In class we are making constructor .After making the constructor we have print(class name.what you have to find .In my case I am finding instance in constructor self.classvar1(note:I know that it is not a class consturctor but let assume).when we inherit the both the class if class B not have any instance like what we have print than interpreter will go to class A .In class A constructor instance is not present than interpreter print the class A instance.
//when we override any thing it will not printed by the interpreter.To solve this problem super() is there.
class A:
	classvar="I am a class variable in 		class A"
//here __init__(self) in a constructor
	def __init__(self):
//here var and classvar  are instance variable
		self.var="I am inside class 			A's constructor"
		self.classvar1="Instance var 			in class A"
//here we are inheriting class A in B
class B(A):
	classvar2="I am in class B"
		def__init__(self) in a constructor
	
	def __init__(self):

//here var and classvar  are instance variable
		super().__init__()
		self.var="I am inside class 			B's constructor"
		self.classvar1="Instance var 			in class B"
//here we are making object
a=A()
b=B()

print(b.classvar1)
//here we are done some  expriment when super().__init__() is after the constructor the output will be different and when we super().__init__() is after  the constructor instance the output will be different 