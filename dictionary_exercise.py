
# Equipment inventory stored in nested dictionaries
equipment = {
    "Tools": {
        "Hammer": "Working",
        "Screwdriver": "Working",
        "Wrench": "Faulty"
    },
    "Cables": {
        "HDMI": "Faulty",
        "Ethernet": "Faulty",
        "USB": "Faulty"
    },
    "Sensors": {
        "Temperature": "Working",
        "Pressure": "Working",
        "Humidity": "Faulty"
    }
}

# Backup dictionary for replacement
backup1 = {
    "Cables": {
        "HDMI": "Working",
        "Ethernet": "Working",
        "USB": "Working"
    }
}

backup2 = {
    "Tools": {
        "Hammer": "Working",
        "Screwdriver": "Working",
        "Wrench": "Faulty"
    }
}

backup3 = {
"Tools": {
        "Hammer": "Working",
        "Screwdriver": "Working",
        "Wrench": "Faulty"
    }
}

print(equipment)
print(backup1)
print(backup2)
print(backup3)


# Final report dictionary
status_report = {}

# Iterate through categories
for category, items in equipment.items():
    working_count = 0
    faulty_count = 0

    # Check each item in the category
    for item, status in items.items():
        if status == "Working":
            working_count += 1
        elif status == "Faulty":
            faulty_count += 1

        # If more than 1 faulty item, break immediately
        if faulty_count > 1:
            print(f"Too many faulty items in {category}, skipping further checks.")
            break

    # After checking items
    if faulty_count > 1:
        # Replace with backup if available
        if category in backup1:
            status_report[category] = "Replaced with backup"
        else:
            status_report[category] = "Too many faults"
        continue  # Skip to next category

    # If no working items, try backup
    if working_count == 0:
        if category in backup:
            status_report[category] = "Replaced with backup"
        else:
            status_report[category] = "No working items"
    else:
        status_report[category] = f"{working_count} items working"

# Display final report
print("\nFinal Equipment Status Report:")
for category, report in status_report.items():
    print(f"{category}: {report}")