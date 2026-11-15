# import pandas as pd

# df=pd.read_csv("customer_churn_business_dataset.csv")
# print(df)

# print("rows : ",df.shape[0])
# print("columns : ",df.shape[1])
# print(df.head())


# df.drop(["payment_method","payment_failures","discount_applied","price_increase_last_3m",
# "support_tickets","escalations","referral_count"],axis=1,inplace=True)

# print(df)

# print("New rows : ",df.shape[0])

# print("New columns : ",df.shape[1])

# print(df.head())
# print(df.tail())

# print(df.columns)

# print(df.info())

# print(df.describe())

# print(df.dtypes)

# ----- missing values -----

# print(df.isnull().sum())

# print(df.isnull().sum().sum())

# print(df.duplicated().sum())

# print(df.drop_duplicates(inplace=True))

# df["complaint_type"]=df["complaint_type"].fillna("Not reported")
# print(df)

# df["annual_fee"]=df["monthly_fee"]*12
# print(df)

# print(df.columns)

# print(df.shape[1])

# df["revenue_per_month"]=df["total_revenue"]/df["tenure_months"]
# print(df)

# print(df[df["age"]>30])

# print(df[df["total_revenue"]>1000])

# print(df[df["churn"]==1])

# print(df["total_revenue"].sum())

# print(df["total_revenue"].mean())

# print(df["total_revenue"].median())

# print(df["total_revenue"].std())
# print(df["total_revenue"].var())
# print(df["total_revenue"].min())

# print(df["age"].mode())

# print(df.sort_values(by=["total_revenue"],ascending=False))

# df["revenue_rank"]=df["total_revenue"].rank(ascending=False)
# print(df)

# print(df.groupby("customer_segment")["total_revenue"].sum())

# print(df.groupby("contract_type")["total_revenue"].mean())

# print(df.groupby("customer_segment")["customer_id"].count())

# report=df.groupby("customer_segment").agg({"customer_id" : "count" , "total_revenue" : "sum",
#                                            "total_revenue" : "mean", "age" : "mean", "churn" : "sum"})

# print(report)

# customer=df[["customer_id" , "gender" , "age" , "customer_segment"]]

# revenue=df[["customer_id" , "monthly_fee" , "total_revenue" , "churn"]]

# print(pd.merge(customer,revenue,on="customer_id"))

# print(pd.merge(customer,revenue,on="customer_id",how="outer"))

# print(pd.merge(customer,revenue,on="customer_id",how="left"))

# print(pd.merge(customer,revenue,on="customer_id",how="right"))

# print(df.corr(numeric_only=True))

# print(df["total_revenue"].corr(df["churn"]))

# print(df.sort_values(by="total_revenue",ascending=False).reset_index)