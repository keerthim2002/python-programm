# import pandas as pd

# data={
#     "Name" : ["Anitha" , "Rahul" , "Meera"],
#     "Salary" : [50000, 45000, 60000],
#     "Department" : ["IT" , "HR" , "IT"]
# }

# df=pd.DataFrame(data)
# print(df)

# df["dept"]=df["Department"]
# print(df)

# df["employee id"]="101"
# print(df)

# df["bonus"]=df["Salary"]*0.1
# print(df)

# df.drop("employee id",axis=1,inplace=True)
# print(df)

# df.drop(["dept","bonus"],axis=1,inplace=True)
# print(df)

# result=df[df["Salary"]>50000]
# print(result)

# result=df[(df["Department"]=="IT")&(df["Salary"]>50000)]
# print(result)

# result=df[(df["Department"]=="IT")|(df["Salary"]>50000)]
# print(result)

# result=df[~(df["Department"]=="IT")]
# print(result)


# result=df[df["Department"].isin(["IT" , "HR"])]
# print(result)

# result=df[df["Name"].str.startswith("A")]
# print(result)

# result=df[df["Name"].str.endswith("l")]
# print(result)

# result=df[df["Name"].str.contains("ul")]
# print(result)


# print(df.isnull())

# print(df.isnull().sum())

# print(df.dropna())

# df["Salary"].fillna(df["Salary"].mean(),inplace=True)
# print(df)

# df["Department"]=df["Department"].fillna("Unknown")
# print(df)

# df.fillna(0,inplace=True)
# print(df)

# data2={
#     "Name" : ["Anitha" , "Rahul" , "Meera"],
#     "Employee id" : [101,102,103]
# }
# df1=pd.DataFrame(data2)
# print(df1)

# inner_join=pd.merge(df,df1,on="Name")
# print(inner_join)

# left_join=pd.merge(df,df1,on="Name",how="left")
# print(left_join)

# right_join=pd.merge(df,df1,on="Name",how="right")
# print(right_join)
# outer_join=pd.merge(df,df1,on="Name",how="outer")
# print(outer_join)