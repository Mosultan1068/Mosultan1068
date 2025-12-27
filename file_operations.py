import os

class filesprocessing:
    # this is an example of the constructor
    def __init__(self, file_name , file_location):
        self.file_name = file_name
        self.file_location = file_location

    #this is just to display the data which was accepted by te
    # constructor above
    def file_details(self):
        return (f" The following will be processed: filename = {self.file_name} ,location= {self.file_location}")

    # this is an example of the deconstreuctor
    def __del__(self):
        return f" file details are {self.file_name}, {self.file_location} has been deleted"

    def create_test_file(self):
        file = open(self.file_name, "w")
        file.write("Customer Name,Feedback\nJohn Wick,Good\n")
        file.close()
        print(f"{file} , file created.")

    def delete_test_file(self):
        file = os.remove(self.file_name)
        print(f"{file} , file deleted.")

file1=filesprocessing("textfile.txt","sharepoint")
print(file1.file_details())
file1.create_test_file()
file1.delete_test_file()