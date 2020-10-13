# instance and class variables



class employee:
    no_of_leaves=5
    pass


ok=employee()
bye=employee()
ok.name="Ok"
ok.salary=654

bye.name="BYE"
bye.salary=6354
print(employee.__dict__)
# instance variable
bye.no_of_leaves=2 
# class variable
employee.no_of_leaves=7
print(employee.__dict__)