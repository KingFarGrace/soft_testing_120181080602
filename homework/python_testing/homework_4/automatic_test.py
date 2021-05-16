from selenium import webdriver
import time

wd = webdriver.Chrome(r'D:\tools\chrome-driver\chromedriver_win32\chromedriver.exe')
wd.get('https://www.jd.com/')

# 测试搜索框功能
search_box = wd.find_element_by_id('key')
search_box.send_keys('笔记本电脑\n')
wd.implicitly_wait(5)
game_computer = wd.find_element_by_xpath('//a[@title=\'游戏本\']')
game_computer.click()
wd.implicitly_wait(5)
computer_list = wd.find_elements_by_xpath('//ul[@data-tpl=\'1\']//li')
for computer in computer_list:
    print(computer.find_element_by_xpath('.//div[@class=\'p-img\']//a[@target=\'_blank\']').get_attribute('href'))
time.sleep(1)
wd.back()
wd.back()

############################################

# # 测试登录页面是否正常运作
# login = wd.find_element_by_xpath('//a[@class=\'link-login\']')
# login.click()
# wd.implicitly_wait(5)
# login_by_account = wd.find_element_by_xpath('//div[@class=\'login-tab login-tab-r\']//a')
# login_by_account.click()
# account_name = wd.find_element_by_id('loginname')
# account_pwd = wd.find_element_by_id('nloginpwd')
# account_name.send_keys('KingFar')
# account_pwd.send_keys('1234567890')
# time.sleep(2)
# wd.find_element_by_id('loginsubmit').click()

############################################

# # 测试侧边栏导航是否正常运作
# mainWindow = wd.current_window_handle
# aside_functions = wd.find_elements_by_xpath('//ul[@class=\'JS_navCtn cate_menu\']//li/a')
# for func in aside_functions:
#     if func.text == '电脑':
#         func.click()
# for handle in wd.window_handles:
#     wd.switch_to.window(handle)
#     if wd.title == '电脑_笔记本_台式机_电脑配件_办公设备-京东':
#         break
# wd.implicitly_wait(5)
# search_box = wd.find_element_by_id('key')
# search_box.send_keys('游戏本\n')
# time.sleep(5)
# wd.close()
# time.sleep(1)
# wd.switch_to.window(mainWindow)

print('测试程序即将退出...')
time.sleep(3)
wd.quit()
