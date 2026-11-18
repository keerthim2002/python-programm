# import pandas as pd

# df=pd.read_csv("retail_sales_exact_columns.csv")
# print(df)

# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.countplot(x=df["Region"],data=df,palette="Set1")
# plt.title("orders by region")
# plt.xlabel("Region")
# plt.ylabel("Count")
# plt.show()


# sns.countplot(x=df["Category"],data=df,palette="Set2")
# plt.title("Number of records in each category")
# plt.xlabel("Category")
# plt.ylabel("count")
# plt.show()

# sns.barplot(x="Region",y="Sales",data=df)
# plt.title("Sales vs region")
# plt.show()

# sns.barplot(x="Category",y="Profit",data=df)
# plt.title("profit vs category")
# plt.show()

# df['Date'] = pd.to_datetime(df['Order Date'], format='%d-%m-%Y')
# df['Month_Name'] = df['Date'].dt.month_name()

# print(df['Month_Name'] ) 

# total_sales=df.groupby("Month_Name")["Sales"].sum()
# print(total_sales)

# sns.lineplot(x="Month_Name",y="Sales",data=df)
# plt.title("Monthly sales trend")
# plt.show()

# total_profit=df.groupby("Month_Name")["Profit"].sum()
# print(total_profit)


# sns.lineplot(x="Month_Name",y="Sales",data=df)
# plt.title("Monthly profit trend")
# plt.show()

# corr=df.corr(numeric_only=True)
# print(corr)

# sns.heatmap(corr,annot=True,cmap="coolwarm")
# plt.title("Correlation heatwarm")
# plt.show()


# sns.pairplot(df[["Sales" , "Profit" , "Quantity" , "Unit Price"]])
# plt.show()



# sns.countplot(x=df["Region"],data=df,palette="Set1",hue="Category")
# plt.title("orders by region")
# plt.xlabel("Region")
# plt.ylabel("Count")
# plt.show()


# sns.barplot(x="Region",y="Profit",data=df,hue="Category")
# plt.title("profit vs region")
# plt.show()
