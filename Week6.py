class Vehicle:
	"""A program to keep a record of your vehicles."""
def __init__(self, make, model, color, fueltype):
	"""Initializing Attributes."""
    self.make=make
	  self.model=model
	  self.color=color
	  self.fueltype=fueltype
  
    def getMake(self):
      return getMake(self)
  
    def getModel(self):
      return getModel(self)

    def getColor(self):
      return getColor(self)

    def getFueltype(self):
      return getFueltype(self)


class Car(Vehicle):
	"""Vehicle type car."""
def __init__(self, make, model, color, fueltype):
	 """Initialize parent class."""
    #super(). __init__(make, model, color, fueltype)
    self.engineSize=engineSize
    self.numDoors=numDoors

     def getEngineSize(self):
      return getEngineSize(self)
 
     def getNumDoors(self):
      return getNumDoors(self)



class Pickup(Vehicle):
    """Vehicle type pickup."""
def __init__(self, make, model, color, fueltype):
    """Initialize parent class."""
    #super(). __init__(make, model, color, fueltype)
    self.cabStyle=cabStyle
    self.bedLength=bedLength

    def getCabStyle(self):
      return getCabStyle(self)

    def getBedLength(self):
       return getBedLength(self)    


def printGarageMenu():
	print("[1] Please add your car.")
	print("[2] Please add your pickup.")
	print("[3] Would you like to see your garage?")
	print("[4] Quit")

menu()
option = int(input("Enter your option: "))

while option != 4:
    if option == 1:
        get.CarInput:
    elif option == 2:
        get.PickupInput:
    elif option == 3:
        
else:
    print("Invalid option.")
print()
menu()

option=int(input("Enter your option: "))

print("Thank you for using our Garage Program.")

def selectOptions()
    options_chosen = []
    options_common = ['powerwindows', 'powerlocks', 'remotestart', 'backupcamera', 'bluetooth', 'cruisecontrol','heatedseats', 'reardefrost']
 
While (True):
    for option in options_common:
	print(f"option}")
    option_chosen = input("Please choose an option to add to your vehicle.")
    if (option_chosen.upper() =="Quit"):
	break
    else:
        options_chosen.append(option_chosen)
	
	
def getCarInput():
  carDetails = {}
  carDetails["make"] = input("What is the make of your car? ")
  carDetails["model"] = input("What is the model of your car? ")
  carDetails["color"] = input("What is the color of your car? ")
  carDetails["fuelType"] = input("What is the fuel type of your car? ")
  carDetails["options"] = selectOptions()
  carDetails["engineSize"] = input("What is the engine size? ")
  carDetails["numDoors"] = input("How many doors does your car have? ")



  def getPickupInput():
  pickupDetails = {}
  pickupDetails["make"] = input("What is the make of your pickup? ")
  pickupDetails["model"] = input("What is the model of your pickup? ")
  pickupDetails["color"] = input("What is the color of your pickup? ")
  pickupDetails["fuelType"] = input("What is the fuel type or your pickup? ")
  pickupDetails["options"] = selectOptions()
  pickupDetails["cabStyle"] = input("What is your cab style? ")
  pickupDetails["bedLength"] = input("What is your bed length? ")

  def virtualGarage(garage):
    for vehicle in garage:
	print(f{vehicle.getMake()}, {vehicle.getModel()}, {vehicle.getColor(), {vehicle.getFueltype()}')
	vehicle.printOptions()						   
        vehicle.display_info()

    
