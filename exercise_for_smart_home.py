'''
exercise for the smart home
'''

power_station= "ON"
pin_code=int(999)

print(pin_code , power_station)

if power_station == "ON" and pin_code == 999:
    print("Tool activated. Proceed with caution")
else:
    print("Safety lock engaged. Tool disabled.")
