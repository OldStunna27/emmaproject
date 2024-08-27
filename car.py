# my name is emmanuel
class Car:
    Make = "Mercedes_Benz"
    Model = "M Class"
    Year = 2014
    Condition = "New"
    Color = "White"
    Body = "SUV"
    Transmission = "Automatic"


    def __init__(self):
        # self.start = start
        # self.reverse = reverse
        # self.drive = drive
        #self.neutral = neutral
        # self.park = park
        #self.drift = drift
        self.welcome()

        

    def welcome(self):
        print("Welcome to our show room, please inspect and choose a brand new Car you want")
        print()
        self.ignition_method()


    def ignition_method(self):
        self.ignition = input("Enter start to turn on the car engine: ")
        
        if self.ignition == "start":
            print("Welcome to your new car, the car engine is starting now")
            print()
            self.landing_page()
        else:
            print("You need to press ignition button to start the car") 

    def landing_page(self):
        car_gears=("Park", "Reverse", "Neutral", "Drive", "Drift")
        for each in car_gears:
            print(each)
        print()
        self.neutral_method()
    
    def neutral_method(self):
        self.neutral = input("Select N for neutral: ")
        
        if self.neutral =="N":
            print("The car is in neutral, please step on the brake")
            self.drive_method()
        else:
            print("Select neutral")


    def drive_method(self):
        self.drive = input("Select D for drive: ")
        
        if self.drive == "D":
            print("The car is moving forward")
            self.park_method()
        else:
            print("Select drive")    
    
    def park_method(self):
        self.park = input("Select park to stop the car: ")
        
        if self.park == "park":
            print("Car parked successfully")
            self.reverse_method()
        else:
            print("Select park")
    
        
    def reverse_method(self):
        self.reverse = input("Select R for reverse: ")
        
        if self.reverse == "R":
            print("The car is moving backward")
            self.temporary_park_method()
        else:
            print("Select reverse")

    def temporary_park_method(self):
        self.park = input("Select park to stop the car: ")
        
        if self.park == "park":
            print("Car parked successfully")
            self.drift_method()
        else:
            print("Select park")

        
    def drift_method(self):
        self.drift = input("Select Drift: ")
        
        if self.drift == "Drift":
            print("The car drift mode is successfully activated")
            self.total_park_method()
        else:
            print("Select drift")

    def total_park_method(self):
        self.total_park = input("Select park: ")

        if self.total_park == "park":
            print("car parked successfully, please turn off your engine")
            self.ignition_method()

motocar=Car()

        
        
        
        
        
        
        
#         driveMode=("start", "drive", "park", "reverse")
#         for each in driveMode:
#             print(each)
#         user = input("Select drive mode: ")
#         if user =="start":
#             print("The car engine is starting now")
#             self.driveCar()
#         else:
#             print("You need to start the car")
#             self.ignition_method()

        
        

    
    
    
    
    
#     def driveCar(self):
#         self.drive = input("Select gear: ")
#         if self.drive == "drive":
#             print("The car is moving now")
#             self.parkCar()
#         else:
#             print("You need to select drive before car can move")
#             self.driveCar()

#     def reverseCar(self):
#         self.reverse = input("Select reverse: ")
#         if self.reverse == "reverse":
#             print("The car is moving backward")
#             self.driveCar()
#         else:
#             print("select gear")
#             self.reverseCar()

#     def parkCar(self):
#         self.park = input("Select park to stop the car: ")
#         if self.park == "park":
#             print("the car parked successfully. Please off your engine")
#             self.selectGear()
        
#         else:
#             print("You need to select park to stop the car")
#             self.parkCar()


#     def reverseCar(self):
#         self.reverse = input("Select reverse: ")
#         if self.reverse == "reverse":
#             print("The car is moving backward")
#             self.parkCar()

#         else:
#             print("select reverse to move the car backward")
#             self.reverseCar()
    
# motocar=Car()

        
#         #self.park = input("Choose park to stop the car: ")     

        

#         #else:
#             #print("Select drive to move the car")
#             #self.onCar()
    
#     #def driveCar(self):
#         #print("The car is moving now")
#         #self.park = input("Choose park to stop the car: ")
#         #if self.park.lower() == "park":
#             #self.parkCar()
#         #else:
#             #print("select park to stop the car")
    
#     #def parkCar():
#         #print("the car is ready to park")
        

#     #def reverseCar():

        








    
    
    

        
        
