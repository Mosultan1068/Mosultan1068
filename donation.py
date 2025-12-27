'''
donation snipit
showing the elif usage
'''

donation_amount=int(input("Enter the donation amount: "))

if donation_amount >0 and donation_amount <=100:
    print("option1")
elif donation_amount >100 and donation_amount <=200:
    print("option2")
elif donation_amount >200 and donation_amount <=300:
    print("option3")
elif donation_amount >300 and donation_amount <=400:
    print("option4")
elif donation_amount >400 and donation_amount <=500:
    print("option5")
elif donation_amount >500:
    print("option6")