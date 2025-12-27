class Patience_Details:
    #the __init__ is known as the constractor
    def __init__(self,name,age,diseas):
        self.name=name
        self.age=age
        self.__diseas=diseas

    def show_basic_info(self):
        print(f"this is the basic information: {self.name} , {self.age} years old ")
        print()

    def show_full_info(self, is_doctor_checked):
        if is_doctor_checked:
            print(f"{self.name} {self.age} {Diseas}")
        else:
            print(f" Access Denied: Thanks")


name = input("enter patience name:")
age = input("enter patience age:")
Diseas = input("enter patience diseas:")

patient1=Patience_Details(name,age,Diseas)
print("Reciptionist Acces")
patient1.show_basic_info()
# patient1.show_full_info(is_doctor_checked = True)


user_role=input("Are you a doctor: (Yes/No)").strip().lower()
if user_role == "yes" or user_role == "y":
    patient1.show_full_info(True)