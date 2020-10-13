# public, private and protected access specifiers






class employee:
    no_of_leaves=5
    _private=7
    __protect=777
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


# public accesss all of them
shivam=employee("shivam",4628,"pin")
pub=shivam.no_of_leaves
print(pub)
# priavte access is only to the same class and it's child
priv=shivam._private
print(priv)
# protected is for ourself
protect=shivam._employee__protect
print(protect)
