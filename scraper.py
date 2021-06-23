
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
# option.add_argument('--ignore-certificate-errors')
# option.add_argument('--ignore-ssl-errors')
# # # Create new Instance of Chrome
# driver = webdriver.Chrome(executable_path=driver_path, options=option)
# driver.implicitly_wait(10)

#---------------for heroku----------------
chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)
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
    try:
        driver.get(url) 
        table=driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div[2]/table')
        row=table.find_elements_by_class_name("title-cell__ZGos")   
        # print(row)
        leet_code=[]
        for div in row:
            title=div.find_element_by_tag_name("a").get_attribute("innerHTML")
            link=div.find_element_by_tag_name("a").get_attribute("href")
            code={
                "title":title,
                "link":link
            }
            leet_code.append(code)
        All_code.append(leet_code) 
      
    except Exception as e:
        print(e.__class__)

def get_code_geeksforgeeks(url):  
    try:
        driver.get(url) 
        table=driver.find_element_by_xpath('/html/body/div[10]/div[4]/div[2]/div[3]')
        row=table.find_elements_by_class_name('problem-block')
        geeks=[]
        for div in row:
            link=div.find_element_by_tag_name("a").get_attribute("href")
            title=div.find_element_by_tag_name("span").get_attribute("innerHTML")
            code={
                "title":title,
                "link":link,
            }
            geeks.append(code)
        All_code.append(geeks)
    except Exception as e:
        print(e.__class__)
        
def WriteFile(All_code):            
    f=open("geeks.txt","w") #create file
    f.write(json.dumps(All_code))
    f.close()
    os.rename('geeks.txt','result_geeks.txt')



def get_all_code(cat):
    get_code_leetcode("https://leetcode.com/tag/"+cat)
    if cat in geeks_link_dict:
        get_code_geeksforgeeks("https://practice.geeksforgeeks.org/explore/?c&page=1&category%5B%5D="+geeks_link_dict[cat])
    else:
        All_code.append([])


get_all_code(str(sys.argv[1]))

WriteFile(All_code)

