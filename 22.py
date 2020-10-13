



class employee:
    no_of_leaves=5
    def __init__(self,aname,asalary,arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f" Name is {self.name} ,salary is {self.salary} and role is {self.role}"


lucario = employee("Lucario",435,"fighting")
shinchan=employee("Shinchan",555,"love")
print(lucario.printdetails())
# instead of doing in instance and class we can apply this for object oriented programming