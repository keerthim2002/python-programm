# import pandas as pd
# from bs4 import BeautifulSoup

# html="""

# <div class="product">
#   <h2>Laptop</h2>
#   <span class="price">55000</span>
# </div>


# <div class="product">
#   <h2>Mobile</h2>
#   <span class="price">25000</span>
# </div>

# <div class="product">
#   <h2>Tablet</h2>
#   <span class="price">18000</span>
# </div>

# """


# soup=BeautifulSoup(html,"html.parser")

# products=soup.find_all("div",class_="product")

# data=[]

# for item in products:
#     name=item.find("h2").get_text(strip=True)
#     price=item.find("span",class_="price").get_text(strip=True)

#     data.append({
#         "product" : name,
#         "price" : int(price)
#     })


# df=pd.DataFrame(data)

# print(df)

# df.to_csv("product.csv",index=False)

