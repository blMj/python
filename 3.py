# ----------------------------for loop-----------------


items=[int,float,'BLMj',5,2,4,5,7,7,3,2,8,5,3]
for item in items:
    if str(item).isnumeric()and item>=4:
        print(item)