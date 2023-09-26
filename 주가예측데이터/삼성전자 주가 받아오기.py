from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options 
import time

#크롬 드라이버 경로 지정
driver = webdriver.Chrome()

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

#웹 페이지 접속
driver.get('https://finance.yahoo.com/')

# //*[@id="yfin-usr-qry"] 검색창 클릭
x_path = '//*[@id="yfin-usr-qry"]'
driver.find_element(By.XPATH, x_path).click()

# 입력 samsung 입력하기
driver.find_element(By.XPATH, x_path).send_keys('005930')
time.sleep(3)

x_path2 = '//*[@id="header-search-form"]/div[2]/div[1]/div/ul[1]/li/div[1]/div[2]'
driver.find_element(By.XPATH, x_path2).click()
time.sleep(3)

x_path3 = '//*[@id="quote-nav"]/ul/li[5]/a/span'
driver.find_element(By.XPATH, x_path3).click()
time.sleep(3)

x_path4 = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[1]/div[1]/div/div/div/span'
driver.find_element(By.XPATH, x_path4).click()
time.sleep(3)

x_path5 = '//*[@id="dropdown-menu"]/div/ul[2]/li[4]/button/span'
driver.find_element(By.XPATH, x_path5).click()
time.sleep(3)

x_path5 = '//*[@id="Col1-1-HistoricalDataTable-Proxy"]/section/div[1]/div[2]/span[2]/a/span'
driver.find_element(By.XPATH, x_path5).click()