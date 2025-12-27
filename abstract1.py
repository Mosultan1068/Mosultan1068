from abc import ABC, abstractmethod

# Abstract class
class student_details(ABC):
    @abstractmethod
    def whoandwhere(self, student_name, class_name):
        pass  # Must be implemented by subclasses

class student_classes(student_details):
    def whoandwhere(self, student_name, class_name):
        print(student_name, class_name)
        print(student_name," : has been alocated a class")

class student_grade(student_details):
    def whoandwhere(self, subject,grade):
        print(f"{subject} is {grade}")

class student_days(student_details):
    def whoandwhere(self,subject,days):
        print(f"{subject} is {days}")

class check_subject(student_details):
    def whoandwhere(self,subject,grade):
        if subject == "History":
            print(f"subject is {subject} and the grade is {grade}")
        else:
            print(f"subject is {subject} and the grade is {grade}")

#this is the object to access the classes
#this first one is to access the student_cllasses class
student = student_classes()
student.whoandwhere(student_name= " Harry Done", class_name = "Maths")

#this is to access the student_grade
grade_awarded = student_grade()
grade_awarded.whoandwhere("History",12)

student_dats = student_days()
student_dats.whoandwhere("History", "Monday12")

# using input as variables
subject = input("Enter subject : ")
grade = input("Enter grade : ")
subject_check = check_subject()
subject_check.whoandwhere(subject,grade)