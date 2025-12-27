class Drone:
    def __init__(self, drone_id, battery_level, location_code, status="Active"):
        self.drone_id = drone_id
        self.battery_level = battery_level  # percentage 0-100
        self.location_code = location_code
        self.status = status  # Active, Inactive, Damaged

    def is_ready(self):
        """Check if the drone is ready for dispatch"""
        if self.status == "Inactive":
            return False, "Inactive"
        if self.status == "Damaged":
            return False, "Damaged"
        if self.battery_level < 20:
            return False, "Low Battery"
        return True, "Ready"


class RescueDrone(Drone):
    """Specialized drone for emergency rescue missions"""
    def __init__(self, drone_id, battery_level, location_code, status="Active", payload_capacity=5.0):
        super().__init__(drone_id, battery_level, location_code, status)
        self.payload_capacity = payload_capacity  # kg

    def dispatch_info(self):
        return (f"Dispatching {self.drone_id} | "
                f"Battery: {self.battery_level}% | "
                f"Location: {self.location_code} | "
                f"Payload: {self.payload_capacity}kg")


def dispatch_mission(drones):
    """
    Main dispatch function that assigns drones to a rescue mission.
    Handles user input and applies all required exception and control logic.
    """
    print("Starting emergency rescue drone dispatch...\n")

    successful_dispatches = 0
    error_count = 0
    max_errors = 3  # Stop after too many errors

    for drone in drones:
        # Skip inactive drones early
        if drone.status == "Inactive":
            print(f"Skipping {drone.drone_id} (status: {drone.status})")
            continue

        ready, reason = drone.is_ready()
        if not ready:
            print(f"Cannot dispatch {drone.drone_id} ({reason})")
            continue

        while True:
            try:
                user_input = input(f"Enter 'Y' to dispatch Drone {drone.drone_id}: ").strip().upper()

                if user_input != 'Y':
                    raise ValueError("Dispatch cancelled by operator")

                # Simulate potential mission-critical calculation (e.g., flight time estimate)
                if drone.battery_level == 0:
                    raise ZeroDivisionError("Cannot calculate flight time with 0% battery")

                print(f"✅ {drone.dispatch_info()}")
                successful_dispatches += 1
                break  # Exit input loop on success

            except EOFError:
                # Happens in some automated testing environments when input ends unexpectedly
                print("❌ Error: EOF when reading a line")
                error_count += 1
            except ValueError as ve:
                print(f"❌ Invalid input: {ve}")
                error_count += 1
            except ZeroDivisionError as zde:
                print(f"❌ Critical error: {zde}")
                error_count += 1
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                error_count += 1

            # Check if too many errors occurred
            if error_count >= max_errors:
                print("Too many dispatch errors. Stopping...")
                return successful_dispatches

            # Ask again if there was an error
            print("Please try again.\n")

    print(f"\nDispatch complete. {successful_dispatches} drone(s) successfully dispatched.")
    return successful_dispatches


# === Sample Drone Fleet ===
fleet = [
    RescueDrone("D001", 85, "ZONE-A"),           # Ready
    RescueDrone("D002", 15, "ZONE-B"),           # Low battery
    RescueDrone("D003", 90, "ZONE-C", "Inactive"),  # Inactive
    RescueDrone("D004", 75, "ZONE-D"),           # Ready
    RescueDrone("D005", 60, "ZONE-A", "Damaged"),   # Damaged
]

# Run the dispatch system
if __name__ == "__main__":
    dispatch_mission(fleet)