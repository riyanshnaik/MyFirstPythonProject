# Program to calculate total and percentage marks for a student

# Marks obtained and maximum marks for each subject
subjects = {
    'Math': (90, 100),
    'Physics': (95, 100),
    'Chemistry': (89, 100),
    'Literature': (72, 75),
    'Drawing': (68, 75)
}

total_obtained = sum(marks[0] for marks in subjects.values())
total_max = sum(marks[1] for marks in subjects.values())

percentage = (total_obtained / total_max) * 100

print(f"Total Marks Obtained: {total_obtained} / {total_max}")
print(f"Percentage: {percentage:.2f}%")
