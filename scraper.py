
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
# # option.add_argument("--incognito")
# option.add_experimental_option("excludeSwitches", ["enable-automation"])
# option.add_experimental_option('useAutomationExtension', False)
# option.add_argument("--disable-blink-features=AutomationControlled") 
# option.add_argument("--headless") 
# # option.add_argument('--ignore-certificate-errors')
# # option.add_argument('--ignore-ssl-errors')
# # # Create new Instance of Chrome
# driver = webdriver.Chrome(executable_path=driver_path, options=option)
# driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#---------------for heroku----------------
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_argument("--disable-blink-features=AutomationControlled") 
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
# driver.implicitly_wait(10)
geeks_link_dict={
"array":"Arrays",
"dynamic-programming":"Dynamic%20Programming",
"string":"Strings",
"math":"Mathematical",
"greedy":"Greedy",
"depth-first-search":"DFS",
"tree":"Tree",
"hash-table":"Hash",
"binary-search":"Binary%20Search",
"breadth-first-Search":"BFS",
"sorting":"Sorting",
"two-pointers":"two-pointer-algorithm",
"backtracking":"Backtracking",
"stack":"Stack",
"design":"Design-Pattern",
"bit-manipulation":"Bit%20Magic",
"graph":"Graph",
"heap-priority-queue":"priority-queue",
"linked-list":"Linked%20List",
"recursion":"Recursion",
"union-find":"union-find",
"sliding-window":"sliding-window",
"trie":"Trie",
"divide-and-conquer":"Divide%20and%20Conquer",
"ordered-set":"Set",
"segment-tree":"Segment-Tree",
"queue":"Queue",
# "line-sweep":
"geometry":"Geometric",
"binary-indexed-tree":"Binary%20Indexed%20Tree",
# brainteaser
# topological-sort
"binary-search-tree":"Binary%20Search%20Tree",
# rolling-hash
# memoization
# database
# binary-tree
"matrix":"Matrix",
"prefix-sum":"prefix-sum",
# monotonic-stack
"game-theory":"Game%20Theory",
"segment-tree":"Segment-Tree",
"hash-function":"Hash",
"shortest-path":"Shortest%20Path",
"doubly-linked-list":"doubly-linked-list",
"merge-sort":"Merge%20Sort",
}

All_code=[]
if(str(path.isfile('result_geeks.txt'))=="True"):
    os.remove('result_geeks.txt')
if(str(path.isfile('geeks.txt'))=="True"):
    os.remove('geeks.txt') 

def get_code_leetcode(url):  
    driver.implicitly_wait(10)
    try:
        driver.get(url)  
        table=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[2]/table/tbody')
        row=table.find_elements_by_tag_name("tr")  
        # print(row)
        leet_code=[]
        for div in row:
            title=div.find_element_by_tag_name("a").get_attribute("innerHTML")
            link=div.find_element_by_tag_name("a").get_attribute("href")
            difficulty=div.find_element_by_class_name("label").get_attribute("innerHTML")
            code={
                "title":title,
                "link":link,
                "difficulty":difficulty
            }
            leet_code.append(code)
        All_code.append(leet_code) 
      
    except Exception as e:
        print(e.__class__)

def get_code_geeksforgeeks(url):  
    driver.implicitly_wait(20)
    try:
        driver.get(url) 
        table=driver.find_element_by_xpath('/html/body/div[10]/div[4]/div[2]/div[3]')
        row=table.find_elements_by_class_name('problem-block')
        
        geeks=[]
        div_count=2
        for div in row:
            link=div.find_element_by_tag_name("a").get_attribute("href")
            title=div.find_element_by_tag_name("span").get_attribute("innerHTML")
           
            # /html/body/div[10]/div[4]/div[2]/div[3]/div[4]/div/div/div/div[1]
            path="/html/body/div[10]/div[4]/div[2]/div[3]/div["+str(div_count)+"]/div/div/div/div[1]"
            difficulty=div.find_element_by_xpath(path).get_attribute("title")
            div_count=div_count+1
            # print(difficulty)
            code={
                "title":title,
                "link":link,
                "difficulty":difficulty
            }
            geeks.append(code)
        All_code.append(geeks)
    except Exception as e:
        print(e.__class__)
# get_code_geeksforgeeks("https://practice.geeksforgeeks.org/explore/?page=1&category%5B%5D=Game%20Theory")
# print(len(All_code[0]))
def WriteFile(All_code):            
    f=open("geeks.txt","w") #create file
    f.write(json.dumps(All_code))
    f.close()
    os.rename('geeks.txt','result_geeks.txt')



def get_all_code(cat):
    All_code.append([cat])
    get_code_leetcode("https://leetcode.com/tag/"+cat)
    if cat in geeks_link_dict:
        get_code_geeksforgeeks("https://practice.geeksforgeeks.org/explore/?c&page=1&category%5B%5D="+geeks_link_dict[cat])
    else:
        All_code.append([])


get_all_code(str(sys.argv[1]))

WriteFile(All_code)

print(All_code)