class Customer:
  name = ""
  lastName = ""
  age = 0

  def addCart(self):
    print("Add to " + self.name +" "+ self.lastName+" 's cart'")

customer1 = Customer()
customer1.name = "Bob"
customer1.lastName = "Baby"
customer1.age = 8
customer1.addCart()

customer2 = Customer()
customer2.name = "Joe"
customer2.lastName = "Smile"
customer2.age = 19
customer2.addCart()

customer3 =Customer()
customer3.name = "Harry"
customer3.lastName = "Potter"
customer3.age = 15
customer3.addCart()

customer4 = Customer()
customer4.name = "Veeran"
customer4.lastName = "Poonsup"
customer4.age = "32"
customer4.addCart()
