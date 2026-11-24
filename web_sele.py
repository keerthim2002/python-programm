# from selenium import webdriver
# from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("https://www.google.com")

# heading=driver.find_element(By.TAG_NAME,"div")
# print(driver.title)
# print(heading.text)
# driver.quit()

# headings=driver.find_elements(By.TAG_NAME,"h1")
# for heading in headings:
#     print(heading.text)
# driver.quit()

# products=driver.find_elements(By.CLASS_NAME,"w3-row")

# for p in products:
#     print(p.text)

# driver.quit()

# button=driver.find_element(By.ID,"top-nav-bar")
# button.click()
# driver.quit()

# button=driver.find_elements(By.ID,"submit")
# for b in button:
#     button.click()
# driver.quit()


# search_box=driver.find_element(By.NAME,"q")
# search_box.send_keys("Python")
# driver.quit()



# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# driver=webdriver.Chrome()

# driver.get("https://www.w3schools.com")

# wait=WebDriverWait(driver,10)
# heading=wait.until(
#     EC.presence_of_element_located((By.TAG_NAME,"h1"))
# )

# print(heading.text)
# driver.quit()


# driver.get("https://www.w3schools.com")

# wait=WebDriverWait(driver,10)
# heading=wait.until(
#     EC.presence_of_all_elements_located((By.TAG_NAME,"h1"))
# )


# for x in heading:
#     print(x.text)

# driver.quit()



# driver.get("https://www.google.com")

# wait=WebDriverWait(driver,10)
# search_box=wait.until(
#     EC.presence_of_element_located((By.NAME,"q"))
# )

# search_box.send_keys("Python")

# driver.quit()




