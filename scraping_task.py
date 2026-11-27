# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# url='https://books.toscrape.com/' 

# responds=requests.get(url,timeout=10)
# print(responds.status_code)

# soup=BeautifulSoup(responds.text,"html.parser")

# books=soup.find_all("article",class_="product_pod")
# print(len(books))

# data=[]

# for book in books:
#     title=book.find("h3").find("a")["title"]

#     price=book.find("p",class_="price_color").text

#     availability_el=book.find("p",class_="alert")
#     availability=availability_el.get_text(strip=True) if availability_el else "n/a"
  
#     data.append({"Title" : title, "Price" : price , "Availibility" : availability})

# print(data)

# df=pd.DataFrame(data)

# print(df.head())

# df["Price"]=(df["Price"].str.replace(r"[^\d.-]",'',regex=True).astype(float))
# print(df.info())

# print("Total books : ",len(df))

# print("average price : ",df["Price"].mean())
# print("maximum price : ",df["Price"].max())
# print("Minimum price : ",df["Price"].min())
# print("Most expensive books : ")
# print(df.loc[df["Price"].idxmax()])


# df.to_csv("books_data.csv",index=False)
# df.to_excel("books_data.xlsx",index=False)