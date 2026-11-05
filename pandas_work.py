# import pandas as pd
# # print("pandas version : ",pd.__version__)

# data= pd.Series([10,20,30,40])
# print(data)
# print(type(data))

# marks=pd.Series([85,90,76,92,68])
# print("first marks : ",marks[0])
# print("average : ",marks.mean())
# print("maximun : ",marks.max())

# marks=pd.Series(
#     [85,90,76,92],
#     index=["Anu" , "Binu", "ciya", "david"]
# )

# print(marks)
# print("anu's mark : ",marks["Anu"])
# print("marks above 80 : ")
# print(marks[marks>80])

# salary={
#     "anitha" : 50000,
#     "Rahul" : 45000,
#     "meera" : 60000
# }

# salary_series=pd.Series(salary)
# print(salary_series)

# montly_sales=pd.Series(
#     [25000,30000,28000],
#     index=["Jan", "Feb" , "Mar"]
# )

# print(montly_sales)
# print(montly_sales["Jan"])

# print(montly_sales.iloc[0])

# print(montly_sales["Jan":"Feb"])
# print(montly_sales[0:2])

#                                     #arithmetic operations

# print(montly_sales+5000)            #broadcasting

# print(montly_sales.mean())
# print(montly_sales.min())
# print(montly_sales.max())

# high_sales=montly_sales[montly_sales>26000]
# print(high_sales)

                                                #data frame

# data={
#     "name" : ["Anitha" , "Rahul" , "meera"],
#     "Age" : [22,24,23],
#     "course" : ["analytics" , "python" , "analytics"]
# }

# df=pd.DataFrame(data)
# print(df)


# print(df.head())           #head- prints first 5 rows by default of dataframe
# print(df.tail())           #TAIL- prints last 5 rows by default
# print(df.shape)
# print(df.columns)         #prints the names of the columns
# print(df.info())          #prints the overall information of the data

# print(df["name"])           #select a single column

                             #df=pd.read_csv("file name with .extension")


# df=pd.read_csv("student.csv")
# print(df)
# print(df.head(4))
# print(df.tail(5))
# print(df.columns)
# print(df.info())
# print(df.shape)


