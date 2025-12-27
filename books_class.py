class Books:

    def __init__(self,author,title,price):
        self.author=author
        self.title=title
        self.price=price
        print(f"This book has been added: {self.author} , {self.title} , {self.price}")

    def __del__(self):
        print(f"This book has been deleted: {self.author} , {self.title} , {self.price}")

    def __del__(self):
        print(f"This book has been deleted: {self.author}, {self.title}, {self.price}")

        # New method to display book details

    def display_details(self):
        print(f"Author: {self.author}")
        print(f"Title: {self.title}")
        print(f"Price: £{self.price}")


add_book1=Books("A B Tom","The Power of Love","35")
add_book1.display_details()
#del add_book1

