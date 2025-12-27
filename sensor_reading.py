
# Function to evaluate a single reading
def evaluate_machine(reading):
    if reading == 0:
        return "Skipped"
    elif reading > 90:
        return "Critical"
    elif reading <= 30:
        return "Maintenance"
    else:
        return "Normal"


# Function to process a list of readings
def process_sensor_readings(readings):
    print("Processing sensor readings...\n")
    for idx, reading in enumerate(readings, start=1):
        status = evaluate_machine(reading)
        print(f"Reading {idx}: {reading}°C -> Status: {status}")

        # Optional: Add alerts or scoring logic
        if status == "Critical":
            print("⚠ ALERT: Immediate attention required!")
        elif status == "Maintenance":
            print("ℹ Scheduled maintenance recommended.")
        elif status == "Skipped":
            print("⏭ Reading skipped (sensor offline).")
        print("-" * 40)


# Example usage
sensor_readings = [0, 25, 45, 92, 30, 88,230]
process_sensor_readings(sensor_readings)


