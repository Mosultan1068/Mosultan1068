


# Current mode value
current_mode = int(input("Enter the mode (1-Normal, 2-Power Saving, 3-Performance): "))

if current_mode == 1:
    print("Normal Mode is active.")
elif current_mode == 2:
    print("Power Saving Mode is active.")
elif current_mode == 3:
    print("Performance Mode is active.")
else:
    print("Invalid Mode")

print("Thanks")



# Store the hour (0–23)
hour = int(input("Enter the hour (0–23): "))

if 5 <= hour < 12:
    greeting = "Morning"
elif 12 <= hour < 17:
    greeting = "Afternoon"
elif 17 <= hour < 21:
    greeting = "Evening"
else:
    greeting = "Night"

print(f"Good {greeting}!")
