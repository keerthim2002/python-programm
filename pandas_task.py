# import pandas as pd

# ===== E-COMMERCE SALES DATA ANALYSIS =====

# data={
#     "Employee" : ['Arun', 'Anu', 'Rahul', 'Meera', 'John',         
#     'Priya', 'David', 'Sara', 'Kevin', 'Neha',         
#     'Arun', 'Meera', 'John', 'Priya', 'David' ],

#     "Region" : [ 'North', 'South', 'West', 'North', 'South',         
#     'West', 'North', 'South', 'West', 'North',         
#     'South', 'West', 'North', 'South', 'West' ],

#     "Product" : [ 'Laptop', 'Mobile', 'Tablet', 'Laptop', 'Mobile',         
#     'Laptop', 'Tablet', 'Mobile', 'Laptop', 'Tablet',         
#     'Mobile', 'Laptop', 'Tablet', 'Mobile', 'Laptop' ],

#     "Sales" : [45000, 30000, 25000, 55000, 35000,         
#     60000, 20000, 40000, 75000, 15000,         
#     32000, 50000, 28000, 42000, 65000 ],

#     "Profit" : [9000, 6000, 5000, 11000, 7000,         
#     12000, 4000, 8000, 15000, 3000,         
#     6500, 10000, 5500, 8500, 13000 ],

#     "Quantity" : [2, 3, 1, 4, 2,5, 1, 3, 4, 1,2, 3, 2, 4, 5 ]
# }

# df=pd.DataFrame(data)
# print(df)

# ----- DISCRIPTIVE STATISTICS -----

# print("The first five records are : ")
# top_five=df.head(5)
# print(top_five)

# print("The last five records are : ")
# last_five=df.tail(5)
# print(last_five)

# print("STATISTICAL SUMMARY")
# print(df.describe())


# print("Total number of sales records : ")
# print(df["Sales"].count())


# print("Average sales amount : ")
# print(df["Sales"].mean())

# print("LARGEST SALES AMOUNT")
# print(df["Sales"].max())

# print("LOWEST SALES AMOUNT")
# print(df["Sales"].min())

# print("AVERAGE PROFIT")
# print(df["Profit"].mean())

# print("MEDIAN SALES AMOUNT")
# print(df["Sales"].median())

# print("Standard deviation of sales : ",df["Sales"].std())

# print("most frequently occuring sales value : ",df["Sales"].mode())

# ===== SORTING AND RANKING ====

# print("ascending order : ",df.sort_values(by="Sales"))

# print("descending order : ",df.sort_values(by="Sales",ascending=False))

# top_five_sales=df.sort_values(by="Sales").head(5)
# print(top_five_sales)

# bottom_three=df.sort_values(by="Sales").tail(3)
# print(bottom_three)

# profit=df.sort_values(by="Profit",ascending=False)
# print(profit)

# print(df.sort_values("Region"))

# df["Sales_Rank"]=df["Sales"].rank(ascending=False)
# print(df)

# print(df.groupby("Region")["Sales"].sum())

# print(df.groupby("Region")["Sales"].mean())
# print(df.groupby("Region")["Sales"].max())
# print(df.groupby("Region")["Sales"].min())

# print(df.groupby("Region")["Profit"].sum())

# print(df.groupby("Region")["Quantity"].sum())

# print(df.groupby("Product")["Sales"].mean())

# print(df.groupby("Product")["Profit"].mean())

# print(df.groupby("Region").agg({"Sales" : "sum", "Profit" : "mean"}))

# print(df["Sales"].corr(df["Profit"]))

