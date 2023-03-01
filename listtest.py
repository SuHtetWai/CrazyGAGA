def store(name, year, quantity, List=None):
    """ This function will show the list """
    if List is None:
        List = []

    List.append("{0} {1} {2}".format(name, year,quantity))
    return List
myShop = store('gaga',2023,3 )
store('suga',2023,5,myShop)
print(myShop)
help(store)

