
class Vehicle:
    def __init__(self, vehicle_id, fuel_level, engine_condition, distance_covered):
        self._vehicle_id = vehicle_id
        self._fuel_level = fuel_level       # private attribute
        self._engine_condition = engine_condition  # private attribute
        self._distance_covered = distance_covered

#we have 3 getters and 3 setters for the values
    # Getters
    @property
    def vehicle_id(self):
        return self._vehicle_id

    @property
    def fuel_level(self):
        return self._fuel_level

    @property
    def engine_condition(self):
        return self._engine_condition

    @property
    def distance_covered(self):
        return self._distance_covered

#every setter is controlled via a conditon , when met the setter is satisfied
 # Setters
    @fuel_level.setter
    def fuel_level(self, new_fuel):
        if new_fuel >= 0:
            self._fuel_level = new_fuel
        else:
            raise ValueError("Fuel level cannot be negative")

    @engine_condition.setter
    def engine_condition(self, new_condition):
        if new_condition in ["Good", "Faulty"]:
            self._engine_condition = new_condition
        else:
            raise ValueError("Engine condition must be 'Good' or 'Faulty'")

    @distance_covered.setter
    def distance_covered(self, new_distance):
        if new_distance >= self._distance_covered:
            self._distance_covered = new_distance
        else:
            raise ValueError("Distance cannot decrease")


# Status check , to check the status of the engine
    def status_report(self):
        if self._engine_condition == "Faulty" or self._fuel_level < 10:
            return f"Vehicle {self._vehicle_id} needs immediate attention!"
        else:
            return f"Vehicle {self._vehicle_id} is operational."




fleet = [
    Vehicle("Truck-1", 10, "Good", 0),
    Vehicle("Truck-2", 8, "Faulty", 5000),
    Vehicle("Truck-3", 15, "Good", 1500)
]

# Loop through fleet and print status
for v in fleet:
    print(v.status_report())
