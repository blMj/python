# single inheritance




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
    
    @classmethod
    def from_str(cls,string):
        pokemon = string.split("-")
        return cls (pokemon[0],pokemon[1],pokemon[2])
        # another method
        # return cls(*string.split("-"))
# new
class programmer(employee):
    no_of_holidays=56
    def __init__(self,aname,asalary,arole,language):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.language=language

    def printprogs(self):
        return f" The programmer name  is {self.name} ,salary is {self.salary} , role is {self.role} and he love {self.language}" 



lucario = employee("Lucario",435,"fighting")
shinchan=employee("Shinchan",555,"love")
harry=programmer("Harry",777,"coding","python")
print(harry.no_of_holidays)
