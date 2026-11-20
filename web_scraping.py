# ===== FETCHING A WEBPAGE =====


# import requests

# url="https://www.amazon.com"
# response=requests.get(url)
# print(response.status_code)
# print(response.text[:500])

# if response.status_code==200:
#     print("Page fetched successfully ")
# else:
#     print("failed to fetch page")

# print("URL : ",response.url)

# print("Encoding : ",response.encoding)

# print("Headers : ",response.headers)

# try:
#     response= requests.get(url,timeout=10)
#     response.raise_for_status()
#     print("website fetched successfully")

# except requests.exceptions.RequestException as e:
#     print("Error :", e )



# import requests
# from bs4 import BeautifulSoup

# url="https://www.google.com"

# response=requests.get(url)
# soup=BeautifulSoup(response.text,"html.parser")
# print(soup)


# html="""
# <html>
# <body>
#   <h1 id="product">Laptop</h1>
#   <h1> WELCOME to python</h1>
#   <p>Learning web scraping</p>
#   <p class="price">rs500</p>
#   <p class="price">rs800</p>
# </body>
# </html>
# """

# soup=BeautifulSoup(html,"html.parser")
# heading=soup.find("h1")
# print(heading.text)

# price=soup.find("p",class_="price")
# print(price.text)

# product=soup.find(id="product")
# print(product.text)

# prices=soup.find_all("p",class_="price")

# for price in prices:
#     print(price.text)


# product=soup.find(id="product")
# print(product.get_text())

# product=soup.find(id="product")
# print(product.get_text(strip=True))       # strip removes spaces before and after the text


# html="""

# <img src="image.jpeg" alt="My Image">
# <a href="https://www.google.com">Visit Website</a>
# """

# soup=BeautifulSoup(html,"html.parser")
# image=soup.find("img")

# print(image.get("src"))
# print(image.get("alt"))

# link=soup.find("a")
# print(link.get("href"))


# first_price=soup.select_one(".price")

# all_prices=soup.select(".price")

# print(first_price.text)

# for price in all_prices:
#     print(price.text)








