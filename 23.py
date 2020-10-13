
# class method
class employee:
    no_of_leaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f" Name is {self.name} ,salary is {self.salary} and role is {self.role}"
# class method is used to give access to change number of leaves using instance variable
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves




lucario = employee("Lucario",435,"fighting")
shinchan=employee("Shinchan",555,"love")
print(lucario.printdetails())
# lucario and shinchan are instance



# for example
lucario.change_leaves(104)
print(employee.no_of_leaves)
#we can change no of leaves by using instance variable for class variable