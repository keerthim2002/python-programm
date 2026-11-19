# ===== DATA VISUALIZATION =====

# matplotlib is a python library used for visualization

# import matplotlib.pyplot as plt
# print(plt.__version__)

# plt.plot([1,2,3],[10,20,30])        # inside the plot fn, in the list first list shows the X- axis and 2nd list show Y-axis
# plt.show()                          # show( is used to show the chart )


# months=["JAN" , "FEB" , "MAR" , "APR"]

# sales=[20000 , 25000 , 30000 , 28000]

# plt.plot(months,sales)
# plt.title("Monthly Sales Analysis")    # used to give the title for the graph
# plt.xlabel("Month")                    # used to give label for x-axis
# plt.ylabel("Sales")                    # used to give the label for y-axis
# plt.show()


# plt.plot(months,sales,marker="o",color="green",linestyle="-.")
# plt.show()

# linestyle(:) - gives dotted line
# linestyle(-.) - give line-dot line
# linestyle(-) - give solid line
# linestyle(--)


# sales=[20000, 30000 , 40000 , 50000]

# profit=[3000 , 6000 , 9000 , 12000]

# plt.scatter(sales,profit)          #scatter chart
# plt.title("Sales vs Profit")
# plt.xlabel("Sales")
# plt.ylabel("Profit")
# plt.show()

# plt.scatter(sales,profit,color="red" , marker="x", s=100)    # s denoted the size of the marker
# plt.show()


# regions=["North" , "South" , "East" , "West"]

# sales=[40000, 35000 , 30000 , 45000]

# plt.bar(regions,sales)                #vertical bar chart
# plt.title("Sales by Region")
# plt.xlabel("Region")
# plt.ylabel("Sales")
# plt.show()
# plt.bar(regions,sales,color="red",width=0.5)
# plt.show()


# plt.barh(regions,sales)          # horizontal bar chart
# plt.show()
# plt.barh(regions,sales,color=["red" , "green" , "blue"])
# plt.barh(regions,sales,height=0.5)
# plt.show()


# values=["Product A" , "Product B" , "Product C"]

# sales=[50,30,20]

# plt.pie(sales,labels=values,autopct='%1.1f%%',explode=[0.1,0,0],startangle=90)    #autopct changes the value to %
# plt.title("Market Share")
# plt.show()

# marks=[45, 55 , 60 , 65 , 70 , 75 , 80 , 85 , 90 , 95]

# plt.hist(marks,bins=5)               # bins provides the number of range           
# plt.title("Marks Distribution")
# plt.xlabel("Marks")
# plt.ylabel("Number of Students")
# plt.show()

# salaries=[25000 , 30000 , 32000 , 40000 , 100000]
# plt.boxplot(salaries)
# plt.title("Salary Distribution")
# plt.ylabel("Salary")
# plt.show()


#line plot - used to find trends

#box plot - used to find outliers

# pie chart - used to find proportion

#scatter plot - used to find reln betyween variables

#bar chart - used to compare variables

# histogram - used to show frequency





# ===== SEABORN =====



# import seaborn as sns
# import matplotlib.pyplot as plt
# import pandas as pd


# data={
#     "Department" : ["IT" , "HR" , "IT" , "FINANCE" , "HR" , "IT"],
#     "Salary" : [50000 , 45000 , 30000 , 48000 , 70000 , 75000]
# }

# df=pd.DataFrame(data)
# sns.countplot(x="Department",data=df,palette="Set1")            #used to count the repeated values and summarizes
# plt.title("Employee count by Department")
# plt.show()


# sns.barplot(x="Department" , y="Salary" , data=df)
# plt.title("Department vs Salary")
# plt.show()


# data={
#     "Month" : ["Jan" , "Feb" , "Mar" , "Apr"],
#     "Sales" : [20000 , 25000 , 30000 , 28000]
# }

# df=pd.DataFrame(data)

# sns.lineplot(x="Month" , y="Sales" , data=df)
# plt.title("Monthly sales trend")
# plt.show()


# data={
#     "Sales" : [100 , 200 , 300 , 400 , 500],
#     "Profit" : [20 , 40 , 60 , 80 , 100],
#     "Discount" : [5 , 10 , 15 , 20 , 25]
# }

# df=pd.DataFrame(data)

# corr=df.corr()

# sns.heatmap(corr, annot=True,cmap="coolwarm")      # shows the reln between the variables
# plt.title("Correlation Heatwarm")
# plt.show()


# data={
#     "Age" : [22 , 25 , 28 , 30 , 35],
#     "Salary" : [25000 , 30000 , 40000 , 45000 , 60000],
#     "Experience" : [1 , 2 , 4 , 5 , 8]
# }

# df=pd.DataFrame(data)

# sns.pairplot(df)
# plt.show()





