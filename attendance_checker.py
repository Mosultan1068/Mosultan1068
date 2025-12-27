'''
To check the students attandence
if < 75% can not enter the exam
else ok to enter the exam
'''
from traceback import print_tb

total_classes=int(input("enter the number of total classes : "))
attended_classes=int(input("enter the number of classes attended: "))

if (total_classes < attended_classes or
        attended_classes < 0
        or attended_classes > total_classes):
    print("Error")
else:
    print("OK to contenue")
percentage_of_attendance=(attended_classes/total_classes)*100
print(f"The Percentage is: {percentage_of_attendance:.0f}% ")
if int(percentage_of_attendance) > 80:
    print(f"OK To Enter the Exam because the percentahe is:  {percentage_of_attendance:.0f}%")
else:
    print("Not OK because the percentage is: " , percentage_of_attendance,"%")