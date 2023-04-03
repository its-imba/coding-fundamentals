import statistics

# Create the class
class Student:
    def __init__(self, name, age, currentClass):
        self.name = name
        self.age = age
        self.currentClass = currentClass
        self.testScores = []

    # Accept test scores and add to list by using extention (in case there are already scores in list)
    def addTestScores(self, score):
        self.testScores.extend(score)

    # Return average of test scores using mean function (clearer/quicker way of calculating average instead of manually using sum & len)
    def averageTestScore(self):
        return statistics.mean(self.testScores)
        
# Create a student object and add test scores on one line
student1 = Student("John", 20, "Science")
student1.addTestScores([55, 70, 85, 90])

# Calculate the average test score
averageScore = student1.averageTestScore()

# Print the average test score
print(f"The average test score of {student1.name} in {student1.currentClass} is {averageScore:.2f}")

# Prints: "The average test score of John in Science is 75.00"