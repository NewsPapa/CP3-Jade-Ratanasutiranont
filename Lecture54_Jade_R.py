#usernameInput = input("Username : ")
#passwordInput = input("Password : ")
#if usernameInput == "admin" and passwordInput == "1234":
#    print("Done !")
#    print("----- iShop -----")
#    print("1. Vat Calculator")
#    print("2. Price Calculator")
#    userSelected = int(input(">>"))
#    if userSelected == 1:
#        price = int(input("Price (THB) : "))
#        vat = 7
#        result = price + (price * vat / 100)
#        print(result)
#    elif userSelected == 2:
#        price1 = int(input("First Product Price : "))
#        price2 = int(input("Second Product Price : "))
#        print(price1 + price2)

def login():
  usernameInput = input("Username : ")
  passwordInput = input("Password : ")
  if usernameInput == "admin" and passwordInput == "1234":
    return(showMenu())
    
def showMenu():
  print("----- iShop -----")
  print("1. Vat Calculator")
  print("2. Price Calculator")
  return(menuSelect())
def menuSelect():
  userSelected = int(input(">>"))
  if userSelected == 1:
    return(vatCalculator())
  if userSelected == 2:
    return(priceCalculator())
def vatCalculator():
  price = int(input("Price (THB) : "))
  vat = 7
  result = price + (price * vat / 100)
  return(result)
def priceCalculator():
  price1 = int(input("First Product Price : "))
  price2 = int(input("Second Product Price : "))
  return(price1 + price2)
print(login())
