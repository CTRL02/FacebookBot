from openpyxl.reader.excel import load_workbook
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

excel_file_path = 'Spreadsheet.xlsx'
workbook = load_workbook(excel_file_path)
sheet = workbook['Sheet1']
urls_column = sheet['A']

service = Service(executable_path="chromedriver.exe")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})
# chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.facebook.com/")
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "pass")
email.send_keys("sjdsjdh2@gmail.com")  # your email here
password.send_keys("1357qweR")  # your password here
login = driver.find_element(By.NAME, "login")
login.click()
WebDriverWait(driver, 10).until(lambda x: x.execute_script("return document.readyState == 'complete'"))
# ProfileClick = driver.find_element_by_xpath("//div[contains(@class, 'x1i10hfl') and contains(@class, 'x1qjc9v5') and "
#                                             "contains(@class, 'xjbqb8w') and contains(@class, 'xjqpnuy') and "
#                                             "contains(@class, 'xa49m3k') and contains(@class, 'xqeqjp1') and "
#                                             "contains(@class, 'x2hbi6w') and contains(@class, 'x13fuv20') and "
#                                             "contains(@class, 'xu3j5b3') and contains(@class, 'x1q0q8m5') and "
#                                             "contains(@class, 'x26u7qi') and contains(@class, 'x972fbf') and "
#                                             "contains(@class, 'xcfux6l') and contains(@class, 'x1qhh985') and "
#                                             "contains(@class, 'xm0m39n') and contains(@class, 'x9f619') and contains("
#                                             "@class, 'x1ypdohk') and contains(@class, 'xdl72j9') and contains(@class, "
#                                             "'x2lah0s') and contains(@class, 'xe8uvvx') and contains(@class, "
#                                             "'xdj266r') and contains(@class, 'x11i5rnm') and contains(@class, "
#                                             "'xat24cr') and contains(@class, 'x1mh8g0r') and contains(@class, "
#                                             "'x2lwn1j') and contains(@class, 'xeuugli') and contains(@class, "
#                                             "'xexx8yu') and contains(@class, 'x4uap5') and contains(@class, "
#                                             "'x18d9i69') and contains(@class, 'xkhd6sd') and contains(@class, "
#                                             "'x1n2onr6') and contains(@class, 'x16tdsg8') and contains(@class, "
#                                             "'x1hl2dhg') and contains(@class, 'xggy1nq') and contains(@class, "
#                                             "'x1ja2u2z') and contains(@class, 'x1t137rt') and contains(@class, "
#                                             "'x1o1ewxj') and contains(@class, 'x3x9cwd') and contains(@class, "
#                                             "'x1e5q0jg') and contains(@class, 'x13rtm0m') and contains(@class, "
#                                             "'x1q0g3np') and contains(@class, 'x87ps6o') and contains(@class, "
#                                             "'x1lku1pv') and contains(@class, 'x1a2a7pz') and contains(@class, "
#                                             "'xzsf02u') and contains(@class, 'x1rg5ohu')]")
# ProfileClick.click()
# WebDriverWait(driver, 10).until(lambda x: x.execute_script("return document.readyState == 'complete'"))
# AllP = driver.find_element_by_xpath('//div[@aria-label="See all profiles" and @class="x1i10hfl xjbqb8w x1ejq31n xd10rxx x1sy0etr x17r0tee x972fbf xcfux6l x1qhh985 xm0m39n x1ypdohk xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r xexx8yu x4uap5 x18d9i69 xkhd6sd x16tdsg8 x1hl2dhg xggy1nq x1o1ewxj x3x9cwd x1e5q0jg x13rtm0m x87ps6o x1lku1pv x1a2a7pz x9f619 x3nfvp2 xdt5ytf xl56j7k x1n2onr6 xh8yej3" and @role="button" and @tabindex="0"]')
# AllP.click()
# WebDriverWait(driver, 10).until(lambda x: x.execute_script("return document.readyState == 'complete'"))

# parent = driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[2]/div[5]/div[2]/div/div/div[1]/div["
#                                       "1]/div/div/div/div/div/div/div/div/div[2]")
# # driver.execute_script("arguments[0].style.border='2px solid red'", parent)
# search_text = "Test2"
# childPage = parent.find_element(By.XPATH, f'//*[contains(text(), "{search_text}")]')
# itsParent = childPage.find_element(By.XPATH, '..')
# print(itsParent.text)

driver.get('https://www.facebook.com/pages/?category=your_pages')
WebDriverWait(driver, 10).until(lambda x: x.execute_script("return document.readyState == 'complete'"))
class_names = "x9f619 x1n2onr6 x1ja2u2z x78zum5 xdt5ytf x193iq5w x1l7klhg x1iyjqo2 xs83m0k x2lwn1j x1y1aw1k xwib8y2 xh8yej3"
Pages = driver.find_elements_by_xpath(f'//div[@class="{class_names}"]')
page_Name = input("Enter Page Name")
message = input("Enter Message to be sent")
for page in Pages:
    a_element = page.find_element_by_xpath('.//a')
    a_text = a_element.get_attribute("aria-label")
    if a_text == page_Name:
        goToMessages = page.find_element_by_xpath('.//span[contains(text(), "Messages")]')
        # driver.execute_script("arguments[0].setAttribute('style', 'background: yellow; border: 2px solid red;');",
        #                       goToMessages)
        goToMessages.click()
        textarea = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "uiTextareaAutogrow")))
        textarea.send_keys(message)
        textarea.send_keys(Keys.ENTER)
# for cell in urls_column:
#     url = cell.value
#     driver.get(url)
#     message = wait.until(
#         EC.element_to_be_clickable((By.XPATH, '//span[contains(@class, "x1lliihq") and text()="Message"]')))
#     Name = driver.find_element(By.CLASS_NAME, 'x1heor9g')
#     message.click()
#     textbox_element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CSS_SELECTOR, '[role="textbox"]'))
#     )
#     textbox_element.send_keys(f"Hi {Name.text}")
#     time.sleep(1)
#     textbox_element.send_keys(Keys.ENTER)
#     time.sleep(1)
#     close = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Close chat"]')))
#     close.click()
#     time.sleep(1)
# driver.quit()
