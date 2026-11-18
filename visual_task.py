# import pandas as pd

# df=pd.read_csv("retail_sales_exact_columns.csv")
# print(df)

# print(df.head(10))

# print(df.tail(5))

# print(df.shape[0])

# print(df.shape[1])

# print(df.isnull().sum())

# print("totyal sales : ",df["Sales"].sum())

# print("total profit : ",df["Profit"].sum())

# print("average sales : ",df["Sales"].mean())

# print("highest sales : ",df["Sales"].max())

# print("lowest sales : ",df["Sales"].min())

# df['Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
# df['Month_Name'] = df['Date'].dt.month_name()

# print(df['Month_Name'] ) 

# monthly_sales=df.groupby("Month_Name")["Sales"].sum()
# print(monthly_sales)



# import matplotlib.pyplot as plt

# plt.plot(monthly_sales.index,monthly_sales.values,marker="o")
# plt.title("Monthly sales trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid()
# plt.show()

# plt.scatter(df["Sales"],df["Profit"],marker="x",s=50)
# plt.title("Sales vs Profit")
# plt.xlabel("sales")
# plt.ylabel("Profit")
# plt.show()

# region=df.groupby("Region")["Sales"].sum()
# print(region)

# plt.bar(region.index,region.values)
# plt.barh(region.index,region.values)
# plt.title("Region wise sales")
# plt.xlabel("Region")
# plt.ylabel("Sales")
# plt.show()


# product=df.groupby("Product")["Sales"].sum()
# print(product)

# max_index=product.values.argmax()
# exp=[0.1 if i==max_index else 0 for i in range(len(product))]

# plt.pie(product.values,labels=product.index,autopct='%1.1f%%',explode=exp,startangle=90)
# plt.show()

# plt.hist(df["Customer Age"],bins=5)
# plt.hist(df["Customer Age"],bins=10)
# plt.title("customer age distribution")
# plt.xlabel("age")
# plt.ylabel("value")
# plt.show()

# plt.boxplot(df["Profit"])
# plt.title("profit distribution")
# plt.ylabel("Profit")
# plt.show()

# region=df.groupby("Region").agg({"Sales" : "sum" , "Profit" : "sum"})
# print(region)

# region.plot(kind="bar")
# plt.title("sales and profit by region")
# plt.xlabel("region")
# plt.ylabel("amount")
# plt.show()


# product_profit=df.groupby("Product")["Profit"].sum()

# most_profit=product_profit.idxmax()

# print("most profitable product : ",most_profit)
# print("total profit : ",product_profit.max())

# data=df[df["Category"].isin(["Electronics" , "Accessories"])]

# category_sales=df.groupby("Category")["Sales"].sum()

# plt.bar(category_sales.index,category_sales.values)
# plt.title("Electronics vs Accessories")
# plt.xlabel("category")
# plt.ylabel("total sales")
# plt.show()

# plt.hist(df["Customer Rating"],bins=5)
# plt.title("customer rating")
# plt.show()

# profit_region=df.groupby("Region")["Profit"].apply(list)

# plt.boxplot(profit_region)
# plt.title("profit distribution across regions")
# plt.grid()
# plt.show()


# plt.scatter(df["Quantity"],df["Profit"],color="red")
# plt.title("quantity vs profit")
# plt.show()

# cat_sales=df.groupby("Category")["Sales"].sum()
# plt.pie(cat_sales.values,labels=cat_sales.index,autopct='%1.1f%%',startangle=90)
# plt.title("category wise sales contribution")
# plt.show()


# plt.plot(monthly_sales.index,monthly_sales.values, marker="o")
# plt.title("monthly sales trend")
# plt.show()



# ===== RETAIL BUSINESS PERFORMANCE ANALYSIS =====




# print("Total revenue : ",df["Sales"].sum())

# print("Total profit : ",df["Profit"].sum())

# region_sales=df.groupby("Region")["Sales"].sum()
# region_profit=df.groupby("Region")["Profit"].sum()



# data=df.groupby("Region")["Profit"].sum()
# print(data)

# plt.bar(data.index,data.values)
# plt.title("Region wise profit")
# plt.xlabel("Region")
# plt.ylabel("Profit")
# plt.show()


# data=df.groupby("Product")["Sales"].sum()

# plt.bar(data.index,data.values)
# plt.title("Product vs sales")
# plt.xlabel("Product")
# plt.ylabel("Sales")
# plt.show()


# cat_sales=df.groupby("Category")["Sales"].sum()
# plt.pie(cat_sales.values,labels=cat_sales.index,autopct='%1.1f%%',startangle=90)
# plt.title("category wise sales contribution")
# plt.show()

# plt.plot(monthly_sales.index,monthly_sales.values,marker="o")
# plt.title("Monthly sales trend")
# plt.xlabel("Month")
# plt.ylabel("Sales")
# plt.grid()
# plt.show()



# plt.scatter(df["Sales"],df["Profit"],marker="x",s=50)
# plt.title("Sales vs Profit")
# plt.xlabel("sales")
# plt.ylabel("Profit")
# plt.show()



# plt.boxplot(df["Profit"])
# plt.title("profit distribution")
# plt.ylabel("Profit")
# plt.show()


# plt.hist(df["Customer Age"],bins=5)
# plt.title("customer age distribution")
# plt.xlabel("age")
# plt.ylabel("value")
# plt.show()
