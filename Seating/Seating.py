import random

# List of student names
students = [
    "Inez", "Ellen", "Wilma", "Axel", "Ronja",  "Lovisa", "Klara", "Marc", 
    "Valter", "Hugo", "Noel", "Molly", "Tilda", "Novalee", "Maja", "Tuva", "Tina",
    "Erik", "Ofelia", "Freja", "Lewis", "Malek", "Texas", "Noah", "Belle", "Ebba","Kelian", "Malek"
]

# 2D list representing the seating arrangement
# Each sublist represents a row in the classroom
seating = [
    [3, 2],  # Back row
    [2, 3, 2],  # Back Middle row
    [2, 3, 2],  # Middle middle row 
    [2, 3, 2],  # Front Middle row
    [2, 2]   # Front row
]

# Function to scramble the student names
def scramble_students(students):
    random.shuffle(students)
    return students

# Function to display the seating arrangement
def display_seating(students, seating):
    student_index = 0
    for row in seating:
        row_display = []
        for seat in row:
            if seat > 0:
                for _ in range(seat):
                    if student_index < len(students):
                        row_display.append(students[student_index])
                        student_index += 1
                    else:
                        row_display.append("Empty")
            else:
                row_display.append("Empty")
        print("Row:", row_display)

# Scramble the student names
scrambled_students = scramble_students(students)

# Display the seating arrangement
display_seating(scrambled_students, seating)