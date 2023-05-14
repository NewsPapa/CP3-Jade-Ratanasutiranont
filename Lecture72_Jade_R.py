MenuList = []
def showbill():
  TotalP = 0
  print("-----Shop-----")
  for number in range(len(MenuList)):
    print(MenuList[number][0])
    TotalP += int(MenuList[number][1])
  print("Toals:",TotalP)  

while True:
  menuName = input("Plese Enter Menu :")
  if(menuName.lower() == "exit"):
    break
  else:
    menuPrice = input("Price :")  
    MenuList.append([menuName,menuPrice])
showbill()
