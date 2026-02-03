class Chai:
      origin = "India"

print(Chai.origin) # after writing (.)dot ,word that refers to nything'll be displayed 

Chai.is_hot = True # instead of TRUE(boolean) ,it can be written nythng
print(Chai.is_hot)


# creating objects from class Chai
ginger = Chai()
print(f"Ginger {ginger.origin}")
print(f"Ginger {ginger.is_hot}")
ginger.is_hot = False

print("Class:", Chai.is_hot)
print(f"Ginger {ginger.is_hot}")
ginger.flavour = "Ginger"
print(ginger.flavour)