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


