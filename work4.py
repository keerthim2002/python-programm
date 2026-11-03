# ===== REAL WORLD PRACTICAL APPLICATION =====

# ----- EMPLOYEE SALARY ANALYSIS -----

# import numpy as np

# salary=np.array([18000, 22000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000])
# print("Average salary : ",np.mean(salary))
# print("highest salary : ",np.max(salary))
# print("lowest salary : ",np.min(salary))
# print("total monthly salary expense : ",np.sum(salary))
# average_salary=np.mean(salary)
# highest_avg_salary=salary[salary>average_salary]
# highest_avg_employee=len(highest_avg_salary)
# print(f"{highest_avg_employee} members have highest salary above the average salary of each {highest_avg_salary}")
# print("standard deviation of salaries is : ",np.std(salary))


# ----- WEEKLY SALES ANALYSIS -----


# sales=np.array([12000, 15000, 18000, 10000, 22000, 25000, 20000])
# print("total weekly sales : ",np.sum(sales))
# print("average daily sales : ",np.mean(sales))

# highest_sales=np.max(sales)
# lowest_sales=np.min(sales)
# high_sales_day=np.argmax(sales)+1
# low_sales_day=np.argmin(sales)+1

# print(f"The highest sale of Rs {highest_sales} is on day {high_sales_day} ")
# print(f"The lowest sale of Rs {lowest_sales} is on day {low_sales_day} ")

# days=np.where(sales>18000)[0]+1
# print("days with sales above 18000 : ",days)
# sorted_sales=np.sort(sales)[::-1]
# print("sorted sales from highest to lowest : ",sorted_sales)


# ----- ATTENDENCE ANALYSIS -----


# attendence=np.array([95, 88, 76, 65, 92, 55, 80, 45, 98, 72])
# high_attend=attendence[attendence>75]
# low_attend=attendence[attendence<60]
# print("attendence above 75% are ",high_attend)
# print("attendence below 60% are ",low_attend)
# print("average of attendence : ",np.mean(attendence))
# print("highest attendence : ",np.max(attendence))
# print("lowest attendence : ",np.min(attendence))

# eligible=attendence[attendence>=75]
# count=len(eligible)
# print(f"{count} number of students are eligible for examination each with attendence {eligible}")


# ----- TEMPERATURE ANALYSIS -----

# temperature=np.array([29, 31, 30, 32, 28, 35, 33])
# print("average temperature : ",np.mean(temperature))
# print("highest temperature : ",np.max(temperature))
# print("lowest temperature : ",np.min(temperature))

# temp_range=np.max(temperature)-np.min(temperature)
# print("the temperature range is : ",temp_range)
# print("standard deviation : ",np.std(temperature))

# days=np.where(temperature>30)[0]+1
# print(f"{days} days have temperature exceeding 30 degree C")


# ----- IMAGE ARRAY BASICS -----


# image_array=np.array([
#     [10,20,30,40,50], 
#     [60,70,80,90,100], 
#     [110,120,130,140,150], 
#     [160,170,180,190,200], 
#     [210,220,230,240,250]
# ])

# print("minimum pixel : ",np.min(image_array))
# print("maximum pixel : ",np.max(image_array))
# print("average pixel intensity : ",np.mean(image_array))

# image_array[image_array<100]=0
# image_array[image_array>=200]=225

# print(image_array)