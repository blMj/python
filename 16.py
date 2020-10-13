# enumerate function

 

l1=["bhindi","aloo","chopstick","chowmein"]

i=1
for item in l1:
    if i%2 is not 0:
        print(f"baby please buy {item}")
    i+=1


for item in l1:
    if i%2 is not 1:
        print(f"baby please buy {item}")
    i+=1




# enumerate function
for index,item in enumerate(l1):
    if index%2==1:
        print(f"baby please buy {item}")



for index,item in enumerate(l1):
    if index%2==0:
        print(f"baby please buy {item}")
