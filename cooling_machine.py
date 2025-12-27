'''
snipit to check if the machine is ok , cooling or stop
'''

#the three possible status of the machine - stage 1
machine_status_1="OK"
machine_status_2="Cooling"
machine_status_3="Stop"

machine_temp=int(input("Please enter the machine temp:"))

#stage2 - need to check the status of the machine

if int(machine_temp) > 0 and int(machine_temp) < 12:
    print(machine_status_1 , ", All Good")
elif int(machine_temp) > 12 and int(machine_temp) < 18:
    print(machine_status_2, ", Needs Attention")
elif int(machine_temp)  > 18:
    print(machine_status_3,", There are issues")
