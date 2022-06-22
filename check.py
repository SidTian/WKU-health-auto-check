from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import schedule
import time
path=r"/home/sidtian/桌面/auto check/chromedriver"
# http://chromedriver.storage.googleapis.com/index.html
def check(): 
    browser = webdriver.Chrome(executable_path = path)
    browser.get("https://once.wku.edu.cn:4500/Account/login")
    time.sleep(2)
    link = browser.find_element(By.CSS_SELECTOR, "#external-login ul li:last-child")
    ids = browser.find_element(By.CSS_SELECTOR, "#external-login ul li:last-child").click()

    time.sleep(2)

    username = browser.find_element(By.ID, "usernameinput").send_keys("1196698")
    password = browser.find_element(By.ID, "password").send_keys("Tian20020606")
    loginBtn = browser.find_element(By.ID, "submit_button").click()

    browser.get("https://once.wku.edu.cn:6006/iForm/04090919F476FB54248E27")

    time.sleep(2)
    js = 'iduo.data.setUIValue("CurrentLocation", "浙江省 温州市 瓯海区")'
    browser.execute_script(js)

    time.sleep(2)
    checkBtn = browser.find_element(By.CSS_SELECTOR, ".van-button--primary").click()
    time.sleep(1)
    confirmBtn = browser.find_element(By.CSS_SELECTOR, ".van-dialog .van-dialog__confirm").click()
    time.sleep(1)
    browser.quit()
    print("打卡成功： "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

schedule.every().day.at("03:30:00").do(check)
print("打卡程序开始")
while True:
    schedule.run_pending()
    interval = random.randint(1, 10) * 600
    time.sleep(interval)
