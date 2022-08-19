class mobile_phone :
  def __init__(self, brand, price, color, is_available) :
    self.brand = brand
    self.price = price
    self.color = color
    self.is_available = is_available
    
  #creating a class function to determine if a mobile is expensive
  def expensive(self) :
    if self.price > 20000:
      return True
    else:
      return False  

my_mobile = mobile_phone("nokia",10500,"red",True)
print(my_mobile.brand)
print(my_mobile.color)
print(my_mobile.price)
print(my_mobile.expensive())
    
