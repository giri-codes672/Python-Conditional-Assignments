# Grade Calculator

def get_grade(percentage):

    if percentage >= 90 and percentage <= 100:
        return "A"

    elif percentage >= 80:
        return "B"

    elif percentage >= 70:
        return "C"

    elif percentage >= 60:
        return "D"

    else:
        return "F"

marks = float(input("Enter your percentage: "))

grade = get_grade(marks)

print("Your Grade is:", grade)
