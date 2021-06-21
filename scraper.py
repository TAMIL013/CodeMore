
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import json
import os
from os import path
from selenium.webdriver.chrome.options import Options
#-------------for localhost-------------------
# driver_path = "./chromedriver.exe"
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

# option = webdriver.ChromeOptions()
# option.binary_location = brave_path
# # # option.add_argument("--incognito") OPTIONAL
# option.add_argument("--headless") 

# # # Create new Instance of Chrome
# driver = webdriver.Chrome(executable_path=driver_path, options=option)

#---------------for heroku----------------
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)



All_code=[]
if(str(path.isfile('result_geeks.txt'))=="True"):
    os.remove('result_geeks.txt')
if(str(path.isfile('geeks.txt'))=="True"):
    os.remove('geeks.txt') 

def get_code_geeksforgeeks(url):  
    try:
        driver.get(url) 
        count_of_problem=0
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        table=soup.find('div',{'id':'problemFeed'})
        row=table.find_all('div',{'class':'problem-block'})
        f=open("geeks.txt","a") #create file
        
        f.write("{")
        for cd in row:
            count_of_problem=count_of_problem+1
            link=cd.find('a', href=re.compile("problems"))
            title=cd.find('span').text
            code={
                'title':title,
                'link':link.get('href')
            }
            All_code.append(code)
            f.write("{'title':'"+title+"','link':'"+link.get('href')+"'}")
        f.write("}")
        f.write("total no of problems:"+str(count_of_problem))
        f.close()
        # print(count_of_problem)
        os.rename('geeks.txt','result_geeks.txt')
    except Exception as e:
        print(e.__class__)
        
    # for i in All_code:
    #     print(i)


url1="https://practice.geeksforgeeks.org/explore/?page"
url2="=1&category%5B%5D="
Main_url=url1+url2+sys.argv[1]

get_code_geeksforgeeks(Main_url)
# print("tamil")
print(All_code)