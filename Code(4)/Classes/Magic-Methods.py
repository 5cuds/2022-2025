
class Students:

    """
    Student Class
    """

    def __init__(self, name, age, grade):
        """
        Initiate a new Student object

        Parameters:
        name (str): Student name
        age (int): Student age
        grade (int): Student grade
        """
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self): # better
        """
        Get a string representation of the Student

        Returns:
        str: String representation of the Student
        """
        return f"Name: {self.name}\nAge: {self.age}\nGrade: {self.grade}"

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age and self.grade == other.grade

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age
    def __add__(self, other):
        return f"Age: {self.age + other.age}\nGrade: {self.grade + other.grade}"

    def __contains__(self, keyword):
        return keyword in self.name

    def __getitem__(self, key):
        if isinstance(key, int):
            return self.name[key]
        elif isinstance(key, str):
            return getattr(self, key)
        else:
            raise TypeError("Index must be an integer or a string")

    def __len__(self):
        return len(self.name)

    

    

student1 = Students("John", 12, 10)
#student1_copy = Students("John", 12, 10)

#print(student1 == student1_copy)

print(len(student1.name))