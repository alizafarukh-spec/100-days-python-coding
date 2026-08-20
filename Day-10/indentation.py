age = 20

if age >= 18:
    print("Adult")

    if age >= 20:
        print("Age is 20 or above")


# Python Indentation Practice Project

print("=== Student Result Checker ===")

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 80:
    grade = "A+"
    message = "Excellent!"

elif marks >= 70:
    grade = "A"
    message = "Very Good!"

elif marks >= 60:
    grade = "B"
    message = "Good!"

elif marks >= 50:
    grade = "C"
    message = "You passed."

else:
    grade = "F"
    message = "You need to work harder."

print("\n--- Result ---")
print("Name:", name)
print("Marks:", marks)
print("Grade:", grade)
print("Message:", message)

# Indentation Practice Program

name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

if marks >= 50:
    print("Congratulations", name)
    print("You have passed!")

    if marks >= 80:
        print("Excellent marks!")

else:
    print("Sorry", name)
    print("You have failed.")

if marks >= 50:
    print("Congratulations", name)
    print("You have passed!")

    if marks >= 80:
        print("Excellent marks!")