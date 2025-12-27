class Person:
    def __init__(self, name, age, city):
        self.name = name  # underscore indicates a "protected" attribute
        self.age = age
        self.city = city

    def introduction(self):
      return f'I am {self.name}, I am {self.age}, I am {self.city}'

    def process_data(self):
        if self.city == "London":
            city_code = "LDN"
            print(f" The city is {city_code}")
        return(city_code)

# Example usage:
person = Person("Alice",'30',"London")
print(person.name)        # Access via getter → Alice
print(person.introduction()) # this prints the method introduction using the person

peron2 = Person("Bob",30,"London")
print(peron2.introduction())

person3 = Person("Mary",22,"London")
print(person3.introduction())


# Correct way to call process_data:
current_city_code = person3.process_data()
print(f"City code returned: {current_city_code}")
