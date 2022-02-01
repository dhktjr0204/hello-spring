from asyncio import sleep
from operator import contains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import openpyxl
# 엑셀파일 생성
wb=openpyxl.Workbook()

#sheet 활성
sheet=wb.active

#데이터 프레임 내 header생성
sheet.append(["이름","가격","도수","용량","고소한 향","화사한 향","맛의 강도","바디감","매운맛"])



#데이터 크롤링 시작
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://www.sooldamhwa.com/damhwaMarket/listing/soju")

#카카오톡 플친 없애기
try:
    driver.find_element(By.CLASS_NAME,'bg-intelligence-close-icon').click()
except:
    pass


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
#바로 넘어가면 url 다 못담아서
time.sleep(2)



#링크들 담기
pages=driver.find_elements(By.XPATH,"//div[@class='MuiGrid-root MuiGrid-item MuiGrid-grid-xs-6 MuiGrid-grid-sm-4 MuiGrid-grid-md-3 MuiGrid-grid-lg-3']/a")
cur_win = driver.current_window_handle # get current/main window

#상세페이지 링크 담기
links=[]
for page in pages:
    try:
        links.append(page.get_attribute("href"))#link 추출

    except:
        pass  

#상세페이지 정보 긁어오기
for link in links:
    driver.get(link)
    time.sleep(1)
    name=driver.find_elements(By.XPATH,"//div[@class='sector first ga_product_name']")[0].text
    try:
        price=driver.find_elements(By.XPATH,"//span[@class='text ga_product_price ga_product_sale_price']")[0].text
    except:
        price=driver.find_elements(By.XPATH,"//span[@class='text originPrice ga_product_price']")[0].text

    degree=driver.find_elements(By.XPATH,"//div[@class='flex']/span")[1].text
    volume=driver.find_elements(By.XPATH,"//div[@class='flex']/span")[2].text
    flavors=[]
    flavors.append(driver.find_elements(By.XPATH,"//div[@class='wrapper']")[0].text)
    flavors.append(driver.find_elements(By.XPATH,"//div[@class='wrapper']")[1].text)
    flavors.append(driver.find_elements(By.XPATH,"//div[@class='wrapper']")[2].text)
    flavors.append(driver.find_elements(By.XPATH,"//div[@class='wrapper']")[3].text)
    flavors.append(driver.find_elements(By.XPATH,"//div[@class='wrapper']")[4].text)
    sheet.append([name,price,degree,volume,flavors[0],flavors[1],flavors[2],flavors[3],flavors[4]])

wb.save("증류주.xlsx")
driver.close()