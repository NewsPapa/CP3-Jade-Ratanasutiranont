systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}
menuList = []

def showBill():
  Totals = 0
  for number in range(len(menuList)):
      Totals += menuList[number][1]
  print("---- My Food----")
  print(menuList[number][0], menuList[number][1])
  print(Totals)

while True:
    menuName = input("Item Name :")
    if(menuName.lower() == "exit"):
        break
    else:
        menuList.append([menuName, systemMenu[menuName]])

print(menuList)
showBill()
