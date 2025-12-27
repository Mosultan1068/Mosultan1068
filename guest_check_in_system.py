'''
this program will help the customers to check in
'''

# just a simple welcome message - step 1
print("==============================================")
print("Welcome to the guest check in system")
print("===============================================")

# step2 = capturing the user data
max_number_of_guests=input("How many guests are checking in? \n")

if max_number_of_guests.isdigit():
    max_number_of_guests == int(max_number_of_guests)
else:
    print("Number of guests must be a number, thanks , exiting")
    exit(10)

# checking and validating the number of gusts

v_guset_count= 0

while int(v_guset_count) < int(max_number_of_guests):
    v_guset_count +=1
    v_guest_name = input("Please enter the guest name: ")
    v_guest_age = int(input("Please enter the guest age: "))
    v_guest_reservations= input("Does the guest have a reservations: (Y/N)")

    v_reservation_number=input("Please enter the reservation number: ")
    if v_reservation_number == None:
        print("Reservation number not found")
        exit(14)
    else:
        print("value is correct")
        print("need to go to the database to validate the reservations")


#checking if the customer is over 18 and has a reservation
    if v_guest_age > 18 and (v_guest_reservations == "y" or v_guest_reservations == "Y"):
        print("Reservations made")
    else:
        print("Reservation can not be made")
        exit(12)




