students_data = [("alice", 10), ("bob", 10), ("eve", 10), ("john", 10)]


def main():
    student_avg = 0
    passing_students = 0
    for student in students_data:

        # status printing
        student_grade = student[1]
        name = student[0]
        if student_grade < 60:
            print(f"student {name} - you failed with grade {student_grade}")
        elif student_grade >= 60 and student_grade < 90:
            print(f"student {name} - you passed with grade {student_grade}")
            passing_students += 1
        else:
            print(f"student {name} - you excellent with grade {student_grade}")
            passing_students += 1

        # avg calc - step 1
        student_avg += student_grade

    # avg calc - final step
    student_avg = student_avg / len(students_data)
    print(f"student_avg: {student_avg}")
    print(f"passing_students: {passing_students}")


main()
