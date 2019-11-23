items = {}
for x in range(1,6):
    items[x] = x
print(items)
input1 = input("What do you want to take, potion or sword? ")
if input1 == "potion":
    items[1] = "potion"
elif input1 == "sword":
    items[1] = "sword"
print(items)
