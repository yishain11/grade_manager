students_data = [("alice", 55), ("bob", 34), ("eve", 70), ("john", 98)]


def main():
    student_avg = 0
    passing_students = 0
    for student in students_data:
        student_grade = student[1]
        name = student[0]
        if student_grade < 60:
            print(f"student {name} - you failed with grade {student_grade}")
        elif student_grade >= 60 and student_grade < 90:
            print(f"student {name} - you passed with grade {student_grade}")
        else:
            print(f"student {name} - you excellent with grade {student_grade}")


main()
