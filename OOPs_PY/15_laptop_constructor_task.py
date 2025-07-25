# Create a class Laptop with: 
# ● Attributes (in constructor): brand, model, price 
# ● Method apply_discount(percentage) → reduce the price 
# ● Method display_info() → print all details 
#  Also create 3 objects with different data and apply discounts on each. 
#  Bonus: Add a default argument for price = 50000 if not given. 

class lap:
    def __init__(self,brand,model,price=50000):
        self.brand=brand
        self.model=model
        self.price=price
    
    def apply_dis(self,per):
        dis=(per/100)*self.price
        self.price -=dis
    
    def display(self):
        print(f"Brand : {self.brand}")
        print(f"Model : {self.model}")
        print(f"Price : {self.price}")
    
    
l1=lap("ASUS","Asus8181",42000)
l2=lap("LENVO","Len7570",49000)
l3=lap("DELL","Del6305")

l1.apply_dis(10)
l2.apply_dis(20)
l3.apply_dis(50)

l1.display()
print() # Just for spacing
l2.display()
print() # Just for spacing
l3.display()
