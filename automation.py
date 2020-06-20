from selenium import webdriver
import time


driver = webdriver.Chrome(executable_path=r"C:\Users\Shivaraj\Downloads\chromedriver_win32(1)\chromedriver.exe")
driver.get("https://www.instagram.com/")
driver.maximize_window()

usernm_ent=driver.find_element_by_name("username").send_keys("shivarajc973@yahoo.com")
passwd_ent=driver.find_element_by_name("password").send_keys("qwerty@123")
login=driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").submit()