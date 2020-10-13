# args and kwargs




def funargs(normal,*ko,**po):
    print(normal)
    for item in ko:
        print(item)
    print("\n Now I would like to introduce some of our heroes")
    for key , value in po.items():
        print(f"{key} is a {value}")



har = ["harry","vivek","om",]
normal = "i am a normal argument and the student are:"
kw = {"harry": "monitor","vivek":"fitness instructor","om":"tutor"}
let = funargs(normal,*ko,**po)
print(let)








