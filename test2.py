ls = [23,51,69,32,47]
data = int(input("enter data do you search"))
index = 0
found = False
while index < len(ls):
    if ls[index] == data:
        found = True
        print(ls)
        break
    index +=1
if not found:
    ls.append(data)
    print(ls)