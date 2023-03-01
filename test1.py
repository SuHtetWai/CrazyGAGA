from math import sqrt
import math
print("press 1 to adding")
print("press 2 to sub")
print("press 3 to mul")
print("press 4 to divide")
userInput = int(input("Please enter your choice ="))
firstNumber =int(input("Enter your firstData ="))
secondNumber = int(input("Enter your secondData ="))
def addfun(firstNumber,secondNumber):
    return firstNumber + secondNumber
def subfun(firstNumber,secondNumber):
    return firstNumber - secondNumber
def mulfun(firstNumber,secondNumber):
    return firstNumber * secondNumber
def divfun(firstNumber,secondNumber):
    return firstNumber / secondNumber
if userInput == 1:
    result = addfun(firstNumber,secondNumber)
elif userInput == 2:
    result = subfun(firstNumber,secondNumber)
elif userInput == 3:
    result = mulfun(firstNumber,secondNumber)
elif userInput == 4:
    result = divfun(firstNumber,secondNumber)
else:
    print("You should enter between my describe")
print("The result is {} {} {} = {}".format(firstNumber,userInput,secondNumber,result))
print("the square root of {} = {} ".format(result,sqrt(result)))
print("the exp of {} = {}".format(result,math.exp(result)))
print("the value of pi",math.pi)
print("the hex of {} = {}".format(result,hex(result)))

