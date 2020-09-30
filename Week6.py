class Vehicle:
	"""A program to keep record of vehicles."""
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

def selectOptions():
    options_common = ['powerwindows', 'powerlocks', 'remotestart', 'backupcamera', 'bluetooth', 'cruisecontrol']
    options_chosen = []


def printMenu():

    print("Welcome to your virtual garage.")
    print("[1] Add a car.")
    print("[2] Add a truck.")
    print("[3] See your garage.")
    print("[4] Exit")


print(int("Please choose an option ."))



def getCarInput():
  carDetails = {}
  carDetails["make"] = input("What is the make? ")
  carDetails["model"] = input("What is the model? ")
  carDetails["color"] = input("What is the color? ")
  carDetails["fuelType"] = input("What is the fuel type? ")
  carDetails["options"] = selectOptions()
  carDetails["engineSize"] = input("What is the engine size? ")
  carDetails["numDoors"] = input("How many doors? ")



  def getTruckInput():
  truckDetails = {}
  truckDetails["make"] = input("What is the make? ")
  truckDetails["model"] = input("What is the model? ")
  truckDetails["color"] = input("What is the color? ")
  truckDetails["fuelType"] = input("What is the fuel type? ")
  truckDetails["options"] = selectOptions()
  truckDetails["cabStyle"] = input("What is the cab style? ")
  truckDetails["bedLength"] = input("What is the bed length? ")

  def virtualGarage(garage):
    print('virtualGarage')


    