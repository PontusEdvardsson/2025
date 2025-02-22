from flask import Flask, render_template
import random

app = Flask(__name__)

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
    [2, 3, 2],  # Middle row 1
    [2, 3, 2],  # Middle row 2
    [2, 3, 2],  # Middle row 3
    [2, 2]   # Front row
]

# Function to scramble the student names
def scramble_students(students):
    random.shuffle(students)
    return students

@app.route('/')
def index():
    scrambled_students = scramble_students(students.copy())
    return render_template('index.html', students=scrambled_students, seating=seating)

if __name__ == '__main__':
    app.run(debug=True)