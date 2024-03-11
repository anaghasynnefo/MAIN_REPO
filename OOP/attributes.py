class vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def start_engine(self):
        print("ENGINE STARTED")

class car:
    def __init__(self,make,model,year,num_doors,fuel_type):
        self.make=make
        self.model=model
        self.year=year
        self.num_doors=num_doors
        self.fuel_type=fuel_type
    def drive(self):
        print("CAR IS MOVING")

class motorcycle:
    def __init__(self,make,model,year,num_wheels,is_sportbike):
        self.make=make
        self.model=model
        self.year=year
        self.num_wheels=num_wheels
        self.is_sportbike=is_sportbike
    def ride(self):
        print("MOTORCYCLE IS CRUISING")

    vehicle_car_instance=car("SWIFT","DEZIRE",2022,4,"BLACK")
    vehicle_motorcycle_instance=("HONDA","DIO",2023,2)

    vehicle_car_instance.start_engine()
    vehicle_car_instance.drive()

    vehicle_motorcycle_instance.start_engine()
    vehicle_motorcycle_instance.ride()
    
    
        
