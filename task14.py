# print("===== STUDENT & EMPLOYEE MANAGEMENT SYSTEM =====")

# marks = [45, 60, 78, 92, 35, 85, 49, 100]
# print("all marks : ",marks)

# passed=[]
# for score in marks:
#     if score>=50:
#         passed.append(score)

# print("passed marks :",passed)

# pass_list=[score for score in marks if score>=50]
# print("pass mark list : ",pass_list)

# dist=[score for score in marks if score>=75]
# print("distinction marks : ",dist)

# squared=[score ** 2 for score in pass_list]
# print("squared passed marks : ",squared)

# def addition(a,b):
#     return a+b

# def averagemarks(mark_list):
#     if len(mark_list)==0:
#         return 0
#     return sum(mark_list)/len(mark_list)

# def grade(score):
#     if score>=90:
#         return"A"
#     elif score>=75:
#         return"B"
#     elif score>=50:
#         return"C"
#     else:
#         return"Fail"

# print("addition :" ,addition(20,30))
# print("average marks : ",averagemarks(marks))

# for score in marks:
#     print(score, "-> grade" ,grade(score))


# def std_details(name,std_id,course):
#     print("name : ",name)
#     print("Student id : ",std_id)
#     print("Course : ",course)

# print(" ===== STUDENT DETAILS =====")

# std_details("Arun", 101, "BCA")
# std_details(name="Anjali",std_id=102,course="BCom")

# def calculate_discount(price, discount=10):
#     discount_amount = price * discount / 100
#     return price - discount_amount


# print(" ===== DISCOUNT CALCULATOR =====")

# print("Price after default 10% discount:",
#       calculate_discount(1000))

# print("Price after 20% discount:",
#       calculate_discount(1000, 20))

# def average_args(*args):
#     if len(args) == 0:
#         return 0
#     return sum(args) / len(args)


# print(" ===== AVERAGE USING *args =====")

# print("Average:", average_args(75, 82, 90, 68, 85))

# def student_profile(**kwargs):
#     print(" ===== STUDENT PROFILE =====")

#     for key, value in kwargs.items():
#         print(key, ":", value)


# student_profile(name="Rahul",age=21,course="BSc Computer Science",city="Kochi")

# class Employee:

#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.department = department
#         self.salary = salary

#     def display_details(self):
#         print("\n===== EMPLOYEE DETAILS =====")
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Department:", self.department)
#         print("Monthly Salary:", self.salary)

#     def annual_salary(self):
#         return self.salary * 12

#     def is_high_earner(self):
#         return self.salary >= 50000


# emp1 = Employee(201, "Priya", "HR", 55000)

# emp1.display_details()

# print("Annual Salary:", emp1.annual_salary())

# if emp1.is_high_earner():
#     print("High Earner: Yes")
# else:
#     print("High Earner: No")

# class Person:

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display_personal_details(self):
#         print("Name:", self.name)
#         print("Age:", self.age)

# class Student(Person):

#     def __init__(self, name, age, student_id, marks):
#         super().__init__(name, age)
#         self.student_id = student_id
#         self.marks = marks

#     def display_student_info(self):
#         print("\n===== INHERITANCE STUDENT DETAILS =====")
#         self.display_personal_details()
#         print("Student ID:", self.student_id)
#         print("Marks:", self.marks)
#         print("Grade:", grade(self.marks))

#     def has_passed(self):
#         return self.marks >= 50


# student1 = Student("Meera", 20, 103, 88)

# student1.display_student_info()

# if student1.has_passed():
#     print("Result: Passed")
# else:
#     print("Result: Failed")


# print("===== MANAGEMENT SYSTEM COMPLETED =====")
