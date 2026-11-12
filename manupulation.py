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



# dataset={
#     "Sales" : [25000,30000,20000,40000,28000],
#     "Profit" : [5000,7000,4000,10000,6000]
# }

# df=pd.DataFrame(dataset)
# print(df)
# print(df.describe())

# print(df["Sales"].count())

# print(df["Sales"].mean())

# print(df["Sales"].std())

# print(df["Sales"].min())
# print(df["Sales"].max())

# print(df["Sales"].median())

# print(df["Sales"].mode())

# print(df.sort_values(by="Sales"))

# print(df.sort_values(by="Sales",ascending=False))

# print(df.sort_values(by=["Sales","Profit"],ascending=[False,True]))

# df["Rank_sales"]=df["Sales"].rank(ascending=False)
# print(df)

# top_sales=df.sort_values(by="Sales",ascending=False).head(3)
# print(top_sales)

# print(df.tail(3))

# df["Region"]=["North","South","east","west","southeast"]
# print(df)

# print(df.groupby("Region")["Sales"].sum())

# print(df.groupby("Region")["Sales"].mean())
# print(df.groupby("Region")["Sales"].min())
# print(df.groupby("Region")["Sales"].max())

# print(df.groupby("Region").agg({"Sales" : "sum", "Profit" : "mean"}))





