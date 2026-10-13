# Program to calculate total, average, percentage and grade of a student
# Marks are read for three subjects (out of 100 each)

# Reading marks of three subjects
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))

# Checking whether all marks are in the range 0 to 100
if m1 < 0 or m1 > 100 or m2 < 0 or m2 > 100 or m3 < 0 or m3 > 100:
    print("\nError: Marks must be between 0 and 100. Please enter valid marks.")
else:
    # Calculating total, average and percentage
    total = m1 + m2 + m3
    average = total / 3
    percentage = (total / 300) * 100

    # Assigning the grade based on percentage
    if percentage >= 70:
        grade = "DISTINCTION"
    elif percentage >= 60:
        grade = "FIRST CLASS"
    elif percentage >= 40:
        grade = "SECOND CLASS"
    else:
        grade = "FAIL"

    # Displaying the result
    print("\n----------- STUDENT RESULT -----------")
    print("Total Marks :", total, "/ 300")
    print("Average     :", round(average, 2))
    print("Percentage  :", round(percentage, 2), "%")
    print("Grade       :", grade)