
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
       
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        table=soup.find('div',{'id':'problemFeed'})
        row=table.find_all('div',{'class':'problem-block'})
        for cd in row:
            
            link=cd.find('a', href=re.compile("problems"))
            title=cd.find('span').text
            code={
                "title":title,
                "link":link.get('href')
            }
            All_code.append(code)
            
        f=open("geeks.txt","w") #create file
        # f.write("'")
        f.write(json.dumps(All_code))
        # f.write("'")
        f.close()
        # print(count_of_problem)
        os.rename('geeks.txt','result_geeks.txt')
    except Exception as e:
        print(e.__class__)
        
    # for i in All_code:
    #     print(i)


# page=1&category%5B%5D=Arrays&category%5B%5D=Dynamic%20Programming

url1="https://practice.geeksforgeeks.org/explore/?page=1"
url2="&category%5B%5D="
# Main_url=url1+url2+sys.argv[1]
def getURL(url1,url2,x):
    Main_url=url1
    category=x.split(',')
    for i in category:
        Main_url=Main_url+url2+i
    return Main_url    
final_url=getURL(url1,url2,str(sys.argv[1]))
# final_url="https://practice.geeksforgeeks.org/explore/?category%5B%5D=Arrays&page=1&category%5B%5D=Arrays"
get_code_geeksforgeeks(final_url)

# print(json.dumps(All_code))