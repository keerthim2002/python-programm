# import numpy as num

# marks=num.array([75,82,68,91,88])
# print(f"marks : {marks}")

# zero=num.zeros(5)
# print("Zeros : ",zero)

# one=num.ones(5)
# print("Ones : ",one)

# list_numbers=num.arange(10,21)
# print("list of numbers : ",list_numbers)

# even=num.arange(2,21,2)
# print("list of even numbers : ",even)

# space=num.linspace(0,100,5)
# print("Linspace : ",space)


# student_marks=num.array([
#     ['student',  'python',  'sql',  'excel'],
#     ['student1',   75,       82,    68,],
#     ['student2',   91,       88,    95,],
#     ['student3',   65,       72,    80,],
# ])
# print(student_marks)

# print("dimension : ",student_marks.ndim)
# print("shape : ",student_marks.shape)
# print("total number of elements : ",student_marks.size)
# print("data type : ",student_marks.dtype)

# print("first mark : ",marks[0])
# print("third mark : ",marks[2])
# print("last mark : ",marks[-1])
# print("second last mark : ",marks[-2])

# marks[1]=90
# print("updated marks : ",marks)
# marks[-1]=95
# print("updated marks : ",marks)

# ages=num.array([18,20,19,21,18])
# print("first age : ",ages[0])
# print("last age : ",ages[-1])
# ages[2]=22
# print("updates ages : ",ages)

# print("shape : ",ages.shape)
# print("size : ",ages.size)
# print("dimension : ",ages.ndim)
# print("data type : ",ages.dtype)




# students = {}

# n = int(input("Enter the number of students: "))

# for i in range(n):
#     name = input("Enter student name: ").strip().title()

#     marks = {}

#     for subject in ["Python", "SQL", "Excel"]:
#         mark = int(input("Enter " + subject + " marks: "))
#         marks[subject] = mark

#     students[name] = marks

# while True:
#     print("\n===== STUDENT MARKS MANAGEMENT SYSTEM =====")
#     print("1. Display All Students")
#     print("2. Search for a Student")
#     print("3. Calculate Total and Average")
#     print("4. Find Overall Topper")
#     print("5. Update Marks")
#     print("6. Add a New Student")
#     print("7. Display Subject-wise Topper")
#     print("8. Exit")

#     choice = input("Enter your choice: ")

#     if choice =="1":
#         for name, marks in students.items():
#             print("\nStudent:", name)

#             for subject, mark in marks.items():
#                 print(subject, ":", mark)

#     elif choice == "2":
#         name = input("Enter student name: ").strip().title()

#         if name in students:
#             print("Student:", name)

#             for subject, mark in students[name].items():
#                 print(subject, ":", mark)
#         else:
#             print("Student not found!")

#     elif choice == "3":
#         for name, marks in students.items():
#             total = sum(marks.values())
#             average = total / 3

#             print("\nStudent:", name)
#             print("Total Marks:", total)
#             print("Average Marks:", round(average, 2))

#     elif choice == "4":
#         if students:
#             topper = max(students,key=lambda name: sum(students[name].values()))

#             print("Overall Topper:", topper)
#             print("Total Marks:", sum(students[topper].values()))
#         else:
#             print("No student records available!")

#     elif choice == "5":
#         name = input("Enter student name: ").strip().title()

#         if name in students:
#             subject = input("Enter subject (Python/SQL/Excel): ").strip().title()

#             if subject in students[name]:
#                 mark = int(input("Enter new marks: "))

#                 if 0 <= mark <= 100:
#                     students[name][subject] = mark
#                     print("Marks updated successfully!")
#                 else:
#                     print("Marks must be between 0 and 100.")
#             else:
#                 print("Invalid subject!")
#         else:
#             print("Student not found!")

#     elif choice == "6":
#         name = input("Enter new student name: ").strip().title()

#         if name in students:
#             print("Student already exists!")
#         else:
#             marks = {}

#             for subject in ["Python", "SQL", "Excel"]:
#                 mark = int(input("Enter " + subject + " marks: "))

#                 if not 0 <= mark <= 100:
#                     print("Invalid marks! Student not added.")
#                     break

#                 marks[subject] = mark

#             if len(marks) == 3:
#                 students[name] = marks
#                 print("New student added successfully!")

#     elif choice == "7":
#         if students:
#             for subject in ["Python", "SQL", "Excel"]:
#                 topper = max(students,key=lambda name: students[name][subject])

#                 print(subject, "Topper:", topper,"| Marks:", students[topper][subject])
#         else:
#             print("No student records available!")

#     elif choice == "8":
#         print("Exiting program...")
#         break

#     else:
#         print("Invalid choice! Try again.")









