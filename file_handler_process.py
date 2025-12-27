import os

class SurveyFileHandler:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def create_test_file(self):
        file = open(self.input_file, "w")
        file.write("Customer Name,Feedback\nJohn Wick,Good\n")
        file.close()
        print("Test file created.")

    def read_file(self):
        if not os.path.exists(self.input_file):
            print("File not found. Please check the folder.")
            return None
        try:
            file = open(self.input_file, "r")
            data = file.read()
            file.close()
            print("File read successfully.")
            if "Customer Name" not in data:
                raise ValueError("Missing required data.")
            return data
        except PermissionError:
            print("Please close the file in Excel and try again.")
        except ValueError as ve:
            print("The file format is not correct. Please upload a correct file.")
            print("Error:", ve)
        except Exception as e:
            print("Something went wrong while reading the file.")
            print("Error:", e)
        return None

    def write_file(self, content):
        try:
            file = open(self.output_file, "w")
            file.write(content)
            file.close()
            print("New file saved successfully.")
        except OSError:
            print("Not enough space. Please free up space and try again.")

handler = SurveyFileHandler("customer_feedback.csv", "survey_summary.csv")
handler.create_test_file()
data = handler.read_file()
if data:
    handler.write_file("Survey Summary\n")
