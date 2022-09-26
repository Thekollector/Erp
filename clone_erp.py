import time
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
s = Service('./chromedriver.exe')
browser = webdriver.Chrome()
browser.get(
    "https://erp.30shine.com/dang-nhap.html?redirect=https://customer.30shine.com/khach-hang/thong-tin-chung.html")

# Đăng nhập
def login():
    txtUser = browser.find_element(By.ID, "username")
    txtUser.send_keys("cskh.quanly")

    txtPass = browser.find_element(By.ID, "password")
    txtPass.send_keys("CSKH@a123")

    txtPass.send_keys(Keys.ENTER)
    time.sleep(2)
login()

# Nhập từng số điện thoại trong file txt
name = open('tel.txt', mode='r', encoding='utf-8')
lines = name.readlines()
for i in range(len(lines)):
    try:
        exist_tag = browser.find_element(By.XPATH, '//input[@value="ĐĂNG NHẬP"]').text
        flag_ex = 1
    except:
        flag_ex = 0

    if flag_ex == 1:
        login()
        find_name = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                         '#app > section > section > main > div > div > div > div > div > div > div:nth-child(1) > div.ant-col.ant-col-8 > form > div > div.ant-col.ant-col-15.ant-form-item-control-wrapper > div > span > span > span > input')))
        find_name.click()
        tele = '0' + lines[i]
        find_name.send_keys(tele)
        find_name.send_keys(Keys.ENTER)

        try:
            elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > section > section > main > div > div > div > div > div > div > div:nth-child(5) > div > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-4 > span')
                                               ))
            flag = 1
        except:
            flag = 0
            # Nếu số điện thoại không có thôn tin, flag = 0
        if flag == 0:
            # SĐT không có thông tin
            browser.refresh()
            print(tele + "-------------")
            f = open("date.txt", "a")
            f.write("-----------" + '\n')
            f.close()
            continue
        else:
            # SĐT có thông tin, in ra ngày gần nhất sử dụng dịch vụ
            date_time = browser.find_element(By.XPATH,
                                             '//*[@id="app"]/section/section/main/div/div/div/div/div/div/div[5]/div/div[1]/div/div[1]/div/div[1]/div[1]/span')
            print(tele + " " + date_time.text)
            f = open("date.txt", "a")
            f.write(date_time.text + '\n')
            f.close()
            browser.refresh()

    else:
        find_name = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,
                                            '#app > section > section > main > div > div > div > div > div > div > div:nth-child(1) > div.ant-col.ant-col-8 > form > div > div.ant-col.ant-col-15.ant-form-item-control-wrapper > div > span > span > span > input')))
        find_name.click()
        tele = '0' + lines[i]
        find_name.send_keys(tele)
        find_name.send_keys(Keys.ENTER)
        # time.sleep(8)
        # 10 or 20
        try:
            elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR,
                                                '#app > section > section > main > div > div > div > div > div > div > div:nth-child(5) > div > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-4 > span')
                                               ))
            # found = browser.find_element(By.CSS_SELECTOR,
            #                              '#app > section > section > main > div > div > div > div > div > div > div:nth-child(5) > div > div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(1) > div.ant-col.ant-col-4 > span')
            flag = 1
        except:
            flag = 0
            # Nếu số điện thoại có thông tin, flag = 1
        # except:
        #     flag = 0
            # Nếu số điện thoại không có thôn tin, flag = 0
        if flag == 0:
            # SĐT không có thông tin
            browser.refresh()
            print(tele + "-------------")
            f = open("date.txt", "a")
            f.write("-----------" + '\n')
            f.close()
            continue
        else:
            # SĐT có thông tin, in ra ngày gần nhất sử dụng dịch vụ
            date_time = browser.find_element(By.XPATH,
                                             '//*[@id="app"]/section/section/main/div/div/div/div/div/div/div[5]/div/div[1]/div/div[1]/div/div[1]/div[1]/span')
            print(tele + " " + date_time.text)
            f = open("date.txt", "a")
            f.write(date_time.text + '\n')
            f.close()
            browser.refresh()
browser.quit()



# WebDriverWait wait = new WebDriverWait(driver, 10);
# WebElement element = wait.until(ExpectedConditions.visibilityOfElementLocated (By.xpath("//input[@id=’name’]")));