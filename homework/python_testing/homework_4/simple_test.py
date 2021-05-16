from selenium import webdriver
import time
# 注册驱动
wd = webdriver.Chrome(r'D:\tools\chrome-driver\chromedriver_win32\chromedriver.exe')
wd.get('https://www.baidu.com')
time.sleep(1)
wd.quit()
