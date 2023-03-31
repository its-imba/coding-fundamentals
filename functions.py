import statistics

data = "100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83"

grades = data.split(',')

grades = list(map(int, grades))

print("Minimum grade: ", min(grades))
print("Maximum grade: ", max(grades))

total = sum(grades)
count = len(grades)
average = round(total / count, 2)

print(f'The average grade is using sum, len & round is: {average}')

average2 = statistics.mean(grades)

print(f"The average grade using statistics.mean is: {average2:.2f}")

median = statistics.median(grades)

print("The median value is: ", median)