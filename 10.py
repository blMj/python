# using with block to open a file


with open("o.txt","r+") as op:
    print(op.readlines())
    