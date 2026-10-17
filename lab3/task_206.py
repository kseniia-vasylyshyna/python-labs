subjects_count = int(input("Enter the number of subjects: "))
total_sym = 0

for i in range(subjects_count):
    grade = int(input(F"Enter the grade for subject {i + 1}: "))
    total_sym += grade

average = total_sym / subjects_count
print(average)
