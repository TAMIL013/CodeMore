
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import json
import os
from os import path

driver_path = "./chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
# # option.add_argument("--incognito") OPTIONAL
option.add_argument("--headless") 

# # Create new Instance of Chrome
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=option)


All_code=[]
if(str(path.isfile('result_geeks.txt'))=="True"):
    os.remove('result_geeks.txt')
  

def get_code_geeksforgeeks(url):  
    driver.get(url) 
    # time.sleep(5) 
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    table=soup.find('div',{'id':'problemFeed'})
    row=table.find_all('div',{'class':'problem-block'})
    f=open("geeks.txt","a") #create file
    
    f.write("{")
    for cd in row:
        link=cd.find('a', href=re.compile("problems"))
        title=cd.find('span').text
        code={
            'title':title,
            'link':link.get('href')
        }
        All_code.append(code)
        f.write("{'title':'"+title+"','link':'"+link.get('href')+"'}")
    f.write("}")
    f.close()
    os.rename('geeks.txt','result_geeks.txt')
    # for i in All_code:
    #     print(i)

# url = "https://practice.geeksforgeeks.org/explore/?page=1&category%5B%5D=Kadane"
url1="https://practice.geeksforgeeks.org/explore/?page"
url2="=1&category%5B%5D="
url=url1+url2+sys.argv[1]
get_code_geeksforgeeks(url)

