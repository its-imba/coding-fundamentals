# Create the class
class Student:
    def __init__(self, name, age, currentClass):
        self.name = name
        self.age = age
        self.currentClass = currentClass
        self.test_scores = []

    def add_test_score(self, score):
        self.test_scores.append(score)

    def average_test_score(self):
        return sum(self.test_scores) / len(self.test_scores)
        
# Creating a student object and adding test scores
student1 = Student("John", 20, "Science")
student1.add_test_score(75)
student1.add_test_score(85)
student1.add_test_score(90)

# Calculating the average test score
average_score = student1.average_test_score()

# Printing the average test score
print(f"The average test score of {student1.name} in {student1.currentClass} is {average_score:.2f}")