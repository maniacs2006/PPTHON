def manage_student_database():  
    students = []
    student_id = 1
    while True:
        name = input("Please enter the student's name (or type 'stop' to finish): ").strip()
        if name.lower() == 'stop':
            break
        if any(name == student[1] for student in students):
            print("This name is already in the list.")
        else:
            students.append((student_id,name))
            student_id += 1

    print("Compleete List of Students (Tuples): ")
    for student in students:
        print(student)

    print("List of Students with IDs: ")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}")

    total_students = len(students)
    print(f"Total number of students: {total_students}")

    total_length = sum(len(student[1]) for student in students)
    print(f"Total length of all student names combined: {total_length}")

    if students:
        student_longest = max(students, key=lambda student: len(student[1]))
        student_shortest = min(students, key=lambda student: len(student[1]))
        
        print(f"The student with the longest name is: {student_longest}")

        print(f"The student with the shortest name is: {student_shortest}")
    else:
        print("No students in the database")

manage_student_database()