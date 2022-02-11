from cgitb import text
from math import degrees
import pandas as pd
import openpyxl
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# 엑셀파일 생성
wb=openpyxl.Workbook()

#sheet 활성
sheet=wb.active

#데이터 프레임 내 header생성
sheet.append(["이름","도수/용량","생산지","설명"])


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://thesool.com/front/find/M000000087/list.do?kind=CD00000145")


#스크롤 끝까지 내리기------------------------------------------------------
SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height

#-------------------------------------------------------------------------------


for i in range(1,13):
    driver.get("https://thesool.com/front/find/M000000084/list.do?searchType=2&searchKey=&searchKind=&levelType=&searchString=&productId=&pageIndex="+str(i)+"&categoryNm=&kind=CD00000142")
    time.sleep(3)
    names=driver.find_elements(By.XPATH,"//div[@class='name']")
    contents=driver.find_elements(By.XPATH,"//span[@class='el-3line']")

    r_names=[]
    for i in names:
        r_names.append(i.text)
        
    r_contents=[]
    for i in contents:
        r_contents.append(i.text)
        

    r_degree=[]
    for i in range(1,11):
        try:
            r_degree.append(driver.find_elements(By.XPATH,"//*[@id='tab1']/div[1]/ul/li["+str(i)+"]/dl/dd/ul/li[3]/div[2]")[0].text)
        except:
            pass
    r_locations=[]
    for i in range(1,11):
        try:
            r_locations.append(driver.find_elements(By.XPATH,"//*[@id='tab1']/div[1]/ul/li["+str(i)+"]/dl/dd/ul/li[1]/div[2]")[0].text)
        except:
            pass
    
    for i in range(0,10):
        try:
            sheet.append([r_names[i],r_degree[i],r_locations[i],r_contents[i]])
        except:
            pass

wb.save("chungju_sooldam.xlsx")
driver.close()