# List of grades
grades = [95, 85, 75, 65]

# Function to calculate average
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to determine letter grade
def determine_letter_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Calculate average and determine the letter grade
average = calculate_average(grades)
letter_grade = determine_letter_grade(average)

# Output the results
print(f"Average Grade: {average:.2f}")
print(f"Letter Grade: {letter_grade}")