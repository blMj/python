# mutiple inheritance




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
        # pokemon = string.split("-")
        # return cls (pokemon[0],pokemon[1],pokemon[2])
        # another method
        return cls(*string.split("-"))
# new 
class player:
    no_of_games=4
    def __init__(self,aname,agame):
        self.name=aname
        self.game=agame
    def printdetails(self):
         return f" Name is {self.name} ,game is {self.game} "
# here coolprogrammer can access both player function and  employee
class coolprogrammer(player,employee):
    language="c++"
    def printlanguage(self):
        print(self.language)
lucario = employee("Lucario",435,"fighting")
shinchan=employee("Shinchan",555,"love")
pika=player("pika",["cricket"])
octa=pika.printdetails()
print(octa)
karan=coolprogrammer("karan",["UNO"])
det=karan.printdetails()
print(det)