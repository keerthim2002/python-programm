# ===== EMPLOYEE DATA ANALYSIS SYSTEM =====

# import numpy as np
# import pandas as pd

# performance_score=np.array([70,75,80,85,90,95])
# print(performance_score)

# print("First value : ",performance_score[0])


# print("Last value : ",performance_score[-1])

# print("Adding bonus marks to all the employees : ",performance_score+5)

# print("Mean")
# print(np.mean(performance_score))

# print("Median")
# print(np.median(performance_score))

# print("Standard deviation")
# print(np.std(performance_score))

# print("Highest Score")
# print(np.max(performance_score))

# print("Lowest Score")
# print(np.min(performance_score))


# new_score=performance_score.reshape(6,1)
# print(new_score)

# bonus=np.array([2,4,6,8,10,12])
# latest_score=performance_score+bonus

# print("Final Score : ",latest_score)

# salarie=pd.Series(
#     [20000,30000,40000,50000,60000,70000],
#     index=["KEERTHI", "RIYA" , "DHIYA" , "RITHU" , "SOORAJ" , "ALWYN" ]
# )

# print(salarie)

# print("Salary of Riya is : ",salarie["RIYA"])


# print("Salaries are increased by 20%. The new salary list is : ")

# added_salary=salarie+ (salarie*0.2)
# print(added_salary)

# print("Average Salary")
# print(salarie.mean())

# print("Highest salary")
# print(salarie.max())

# print("employees earning above 42000 are ")
# print(salarie[salarie>42000])



# df=pd.read_csv("employees.csv")
# print(df)

# print("Initial records")
# print(df.head())

# print("Column names are ")
# print(df.columns)

# print("Specific columns are ")
# print(df[["Name" , "Salary" , "Age"]])


# print("Employees earning salary more than 45000 are ")
# print(df[df["Salary"]>45000])

# print("Employee details of IT department ")
# print(df[df["Department"]=="IT"])

# df["Annual Salary"]=df["Salary"]*12
# print(df)

# df["Bonus"]=df["Bonus"].fillna(0)
# print(df)

# df.drop("Age",axis=1,inplace=True)
# print(df)

# print("High earning employees are ")
# print(df[df["Salary"]>40000])


# data={
#     "Department" : ["cyber" , "Quality assurance" , "sales", "marketing"],
#     "location" : ["Kochi" , "Kollam" , "Kannur" , "Trivandrum"]
# }

# df1=pd.DataFrame(data)
# print(df1)

# Final_list=df.merge(df1,on="Department",how="inner")
# print(Final_list)