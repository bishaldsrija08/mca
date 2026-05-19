"""
Create a base class University that contains any foru instance variables, initilizer to initialize the value of attributes an a method to display those values. Create two sub classes college and college2 that contains instance attribute in it. And display their values through the child class.
"""

class University:
    def __init__(self, name, location, established_year, ranking):
        self.name = name
        self.location = location
        self.established_year = established_year
        self.ranking = ranking
        
    def display_info(self):
        print(f"University Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Established Year: {self.established_year}")
        print(f"Ranking: {self.ranking}")

class College1(University):
    def __init__(self, name, location, established_year, ranking, department):
        super().__init__(name, location, established_year, ranking)
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Department: {self.department}")

class College2(University):
    def __init__(self, name, location, established_year, ranking, program):
        super().__init__(name, location, established_year, ranking)
        self.program = program

    def display_info(self):
        super().display_info()
        print(f"Program: {self.program}")

# Example usage
college1 = College1("College A", "City X", 1990, 5, "Computer Science")
college2 = College2("College B", "City Y", 1985, 3, "Business Administration")
college1.display_info()
print()
college2.display_info()