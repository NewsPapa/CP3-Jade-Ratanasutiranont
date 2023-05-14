MenuList = []
PriceList = []
def showbill():
  TotalP = 0
  print("-----Shop-----")
  for number in range(len(MenuList)):
    print(MenuList[number],PriceList[number])
    TotalP += int(PriceList[number])
  print("Toals:",TotalP)  

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
    menuPrice = input("Price :")  
    MenuList.append(menuName)
    PriceList.append(menuPrice)
showbill()
