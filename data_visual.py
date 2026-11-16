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