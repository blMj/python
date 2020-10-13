# class method as alternative

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




lucario = employee("Lucario",435,"fighting")
shinchan=employee("Shinchan",555,"love")
print(lucario.printdetails())
# lucario and shinchan are instance
lugia = employee.from_str("Lugia-554-water")
print(lugia.name)

# for example
lucario.change_leaves(104)
print(shinchan.no_of_leaves)
print(employee.no_of_leaves)