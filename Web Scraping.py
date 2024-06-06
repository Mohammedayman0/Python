#!/usr/bin/env python
# coding: utf-8

# In[67]:


from selenium import webdriver
from selenium.webdriver.common.by import By


# In[45]:


# from bs4 import BeautifulSoup
# import requests
# import time
# import datetime

# import smtplib


# In[46]:


# URL = 'https://www.amazon.com/Funny-Data-Systems-Business-Analyst/dp/B07FNW9FGJ/ref=sr_1_3?dchild=1&keywords=data%2Banalyst%2Btshirt&qid=1626655184&sr=8-3&customId=B0752XJYNL&th=1'

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

# page = requests.get(URL, headers=headers)

# soup1 = BeautifulSoup(page.content, "html.parser")

# soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

# title = soup2.find(id='productTitle').get_text()

# price = soup2.find(id='priceblock_ourprice').get_text()


# print(title)
# print(price)


# In[55]:


#driver=webdriver.Firefox(executable_path='E:\Data\geckodriver-v0.34.0-win64\geckodriver.exe')
#driver=webdriver.Firefox(executable_path=r"‪E:\Data\geckodriver-v0.33.0-win642\geckodriver.exe")


# In[68]:


driver=webdriver.Chrome()

driver.get("https://www.amazon.eg/s?k=samsung+phone&crid=5KAZKWTPF1EV&sprefix=samsung+phone%2Caps%2C204&ref=nb_sb_noss_1")


# In[69]:


titles=driver.find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")
for title in titles:
    print(title.text)


# In[70]:


prices=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")
for price in prices:
    print(price.text)


# In[71]:


image=driver.find_elements("xpath","//img[@class='s-image']")
for img in image:
    print(img.get_attribute('src'))


# In[72]:


products=driver.find_elements(By.XPATH,"//span[@class='a-size-base-plus a-color-base a-text-normal']")

prices=driver.find_elements(By.XPATH,"//span[@class='a-price-whole']")


for i in products:
    print(i.text)
    
for i in prices:
    print(i.text)
    


# In[74]:


import csv
with open('amazon_products.csv','w',encoding='utf-8',newline='')as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=',')
    csvwriter.writerow(['المنتجات','prices'])
    for i in range(0,len(prices)):
        csvwriter.writerow([products[i].text,prices[i].text])
        


# In[ ]:





# In[ ]:





# In[ ]:




