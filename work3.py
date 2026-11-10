# import numpy as np

# ===== ARRAY CREATION =====

# num=np.arange(1,21)
# print(num)
# print(num.shape)
# print(num.ndim)
# print(num.size)
# print(num.dtype)

# ===== EVEN AND ODD NUMBERS =====

# numbers=np.arange(1,51)
# print(numbers)

# odd_num=np.arange(1,51,2)
# print(odd_num)

# even_num=np.arange(2,51,2)
# print(even_num)

# print(odd_num.size)
# print(even_num.size)

# ===== ARRAY INDEXING AND SLICING =====

# numbers=np.array([12, 25, 38, 45, 56, 67, 78, 89, 90, 100])
# print(numbers)

# print(numbers[:3])
# print(numbers[7:])
# print(numbers[2:6])
# print(numbers[::-1])
# numbers[4]=99
# print(numbers)

# ===== CREATE A MATRIX =====

# matrix=np.arange(1,10).reshape(3,3)
# print(matrix)
# print("first row : ",matrix[0])
# print("last column : ",matrix[:,2])
# print("diagonal elements : ",np.diagonal(matrix))
# sum_matrix=np.sum(matrix)
# print(sum_matrix)

# ===== RESHAPE AN ARRAY =====

collection=np.arange(1,25)
# print(collection)

# matrix=collection.reshape(4,6)
# print(matrix)
# matrix_2=collection.reshape(6,4)
# print(matrix)
# matrix_3=collection.reshape(2,12)
# print(matrix_3)

# print(matrix.shape)
# print(matrix_2.shape)
# print(matrix_3.shape)


# for rows,cols in [(4,6), (6,4), (2,12)]:
#     result=collection.reshape(rows,cols)
#     print(f"shape {rows} x {cols} : ")                   #another way
#     print(result)
#     print("shape : ",result.shape)


# ===== ARRAY OPERATIONS =====

# a=np.array([10,20,30,40,50])
# b=np.array([2,4,5,8,10])

# print("addition : ",a+b)
# print("subtraction : ",a-b)
# print("multiplication : ",a*b)
# print("division : ",a/b)
# print("exponential : ",a**b)


# ===== ARRAY JOINING =====

# a=np.array([
#     [1,2],
#     [3,4]
# ])
# b=np.array([
#     [5,6],
#     [7,8]
# ])
# print("joined : ",np.concatenate((a,b)))
# print("vertical stack : ",np.vstack((a,b)))
# print("horizontal stack : ",np.hstack((a,b)))

# print("axis 0 joined : ",np.concatenate((a,b),axis=0))
# print("axis 1 joined : ",np.concatenate((a,b),axis=1))

# ===== SORTING AND SEARCHING =====

# num=np.array([45, 12, 89, 34, 67, 23, 90, 56])
# print("ascending order : ",np.sort(num))
# print("descending order : ",np.sort(num)[::-1])

# higher_index=np.argmax(num)
# lower_index=np.argmin(num)
# print(higher_index)
# print(lower_index)

# if 67 in num:
#     print("the number 67 is in the array")
# else:
#     print("67 is not in the array")


# ===== FILTERING VALUES =====

# salary=np.array([18000, 25000, 32000, 45000, 28000, 55000, 60000, 22000, 75000, 40000])
# greater_salary=salary[salary>30000]
# print(greater_salary)

# less_salary=salary[salary<25000]
# print(less_salary)
# print("salary between 25000 and 50000 are : ",salary[(salary>=25000)&(salary<=50000)])

# employees=np.sum(salary>40000)
# print(employees)

# ===== UNIQUE VALUES =====

# unique_values=np.array([10, 20, 30, 20, 40, 10, 50, 30, 60, 20])
# print("unique values are : ",np.unique(unique_values))

# values,count=np.unique(unique_values,return_counts=True)
# print(f"Values : {values}, occurance : {count}")

# print("duplicate values : ",values[count>1])


# ===== MATHEMATICAL ANS STATISTICAL OPERATIONS ====

# ----- STUDENT MARK ANALYSIS -----

# marks=np.array([78, 85, 92, 45, 67, 89, 55, 76, 95, 62])

# print("total : ",np.sum(marks))
# print("Average : ", np.mean(marks))
# print("Highest mark : ",np.max(marks))
# print("Lowest mark : ",np.min(marks))
# print("Median : ",np.median(marks))
# print("Standard deviation : ",np.std(marks))

# ----- VARIENCE AND STANDARD DEVIATION -----

# a=np.array([50,50,50,50,50])
# b=np.array([40, 45, 50, 55, 60])
# c=np.array([10, 30, 50, 70, 90])
# print("mean of a : ",np.mean(a))
# print("varience of a : ",np.var(a))
# print("std of a : ",np.std(a))

# print("mean of b : ",np.mean(b))
# print("varience of b : ",np.var(b))
# print("std of b : ",np.std(b))

# print("mean of c : ",np.mean(c))
# print("varience of c : ",np.var(c))
# print("std of c : ",np.std(c))

# var_a=np.var(a)
# print(var_a)
# var_b=np.var(b)
# print(var_b)
# var_c=np.var(c)
# print(var_c)

# highest_varience=max(var_a,var_b,var_c)
# print("Highest varience among the datasets is : ",highest_varience)

# ----- SUBJECT-WISE AVERAGE -----

# marks_matrix=np.array([
#     [80, 75, 90], 
#     [65, 85, 70], 
#     [90, 95, 88], 
#     [55, 60, 65], 
#     [75, 80, 85]
# ])
# print(marks_matrix.ndim)
# print(marks_matrix.shape)

# print("sum of marks of each students are : ",np.sum(marks_matrix,axis=1))
# print("Average of marks of each student are : ",np.mean(marks_matrix,axis=1))

# print("Average of each subjects : ",np.mean(marks_matrix,axis=0))

# total_score=np.sum(marks_matrix,axis=1)
# highest_score=np.max(total_score)
# highest_student=np.argmax(total_score)
# print(f"the {highest_student+1} student score the highest score with {highest_score} score ")


#----- RANDOM NUMBER GENERATION -----
# np.random.seed(10)
# random_num=np.random.randint(1,101,size=20)
# print(random_num)
# print("maximum number is : ",np.max(random_num))
# print("minimum number is : ",np.min(random_num))
# print("mean of the array is : ",np.mean(random_num))
# above_50 = random_num[random_num>50]
# print(above_50)
# print("Count greater than 50 are : ",above_50.size)
# print(np.sort(random_num))

# ----- PERCENTAGE AND RANKING -----

# marks=np.array([
#     [25,44,89,75],
#     [99,75,86,93],
#     [85,96,72,63],
#     [82,91,90,70],
#     [99,100,46,80]
# ])

# print(marks)
# total_marks=np.sum(marks,axis=1)
# print("Total marks of each students are : ",total_marks)
# print(type(total_marks))
# l=[10,20,30]
# print(l)
# s=marks.shape
# print(type(s))
# percentage=(np.sum(marks,axis=1)/(s[1]*100))*100
# print(f"percentage of the marks of each students are {percentage}%")

# score=np.sort(percentage)
# print(score)
# max_score=np.max(percentage)
# max_std=np.argmax(percentage)
# print(f"{max_score}% is the toppest percentage secured by {max_std+1}nd student")
