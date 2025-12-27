class Vehicle:
    def __init__(self, vehicle_id, distance_traveled, fuel_level, engine_status):
        self.__vehicle_id = vehicle_id          # Private attribute
        self.__distance_traveled = distance_traveled
        self.__fuel_level = fuel_level          # Percentage
        self.__engine_status = engine_status    # "OK" or "Damaged"

    # Getters and Setters for encapsulation
    def get_vehicle_id(self):
        return self.__vehicle_id
    # this is a getter
    def get_distance_traveled(self):
        return self.__distance_traveled
    # this is a setter
    def set_distance_traveled(self, distance):
        self.__distance_traveled = distance
    # this is a getter
    def get_fuel_level(self):
        return self.__fuel_level
    #this is a setter
    def set_fuel_level(self, fuel):
        self.__fuel_level = fuel
    #this is a getter
    def get_engine_status(self):
        return self.__engine_status
    #this is a setter
    def set_engine_status(self, status):
        self.__engine_status = status

    # Polymorphic method
    def check_maintenance(self):
        raise NotImplementedError("Subclasses must implement this method")

# Subclasses from vehicle with their own maintenance logic
# also uses the polymorphic method above
# therefore, this is a subclass of Vehicle + check_maintenance method.
class Truck(Vehicle):
    def check_maintenance(self):
        return self.get_distance_traveled() > 1000  # Needs service after 1000 km

class Bike(Vehicle):
    def check_maintenance(self):
        return self.get_distance_traveled() > 500   # Needs service after 500 km

class Drone_1(Vehicle):
    def check_maintenance(self):
        return self.get_distance_traveled() > 200   # Needs service after 200 km



    # Create mixed vehicle list
    fleet = [
        Truck("T001", 1200, 30, "OK"),
        Bike("B001", 300, 50, "OK"),
       # Drone_1("D001", 250, 80, "OK"),
       # Drone_1("D1000", 300, 780, "OK"),
        Truck("T002", 800, 10, "Damaged")  # Urgent attention
            ]

    # Iterate and check maintenance
    for vehicle in fleet:
        print(f"Checking vehicle {vehicle.get_vehicle_id()}...")

        # Urgent attention check
        if vehicle.get_fuel_level() < 15 or vehicle.get_engine_status() == "Damaged":
            print(f"⚠ Vehicle {vehicle.get_vehicle_id()} needs urgent attention!")
            break  # Stop checking immediately

        # Regular maintenance check
        if vehicle.check_maintenance():
            print(f"Vehicle {vehicle.get_vehicle_id()} needs scheduled maintenance.")
        else:
            print(f"Vehicle {vehicle.get_vehicle_id()} is fine.")
