UserName = input("Username :")
PassWord = input("Password :")
if UserName == "Admin" and PassWord == "1234":
  print("------ New's Stone Shop ------")
  print("List Item")
  print("1. Red Gem Stone > 10 THB / EA ")
  print("2. Blue Gem Stone > 35 THB / EA ")
  print("3. Yellow Gem Stone > 15 THB / EA ")
  red = 10
  blue = 35
  Yellow = 15
  userSelected = int(input("Choose :"))
  if userSelected == 1:
    Product = red
    Quality = int(input("EA ?"))
    Result = Product*Quality
    print("Total Buy Red Gem Stone: ",Quality," EA :",Result,"THB")
  if userSelected == 2:
    Product = blue
    Quality = int(input("EA ?"))
    Result = Product*Quality
    print("Total Buy Blue Gem Stone: ",Quality," EA :",Result,"THB")
  if userSelected == 3:
    Product = Yellow
    Quality = int(input("EA ?"))
    Result = Product*Quality
    print("Total Buy Yellow Gem Stone: ",Quality," EA :",Result,"THB")
  else:
    print("ERROR")
else:
    print("ERROR")
