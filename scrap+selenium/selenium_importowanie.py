import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

SCIEZKA_PLIKOW = 'C:\Projects\presta-lamp-shop\scrap+selenium'


s = Service("C:\Apps\chromedriver_win32\chromedriver.exe")

driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("http://localhost:8080/admin123")

driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()

driver.find_element(By.XPATH, '//*[@id="email"]').send_keys('lamper@lamper.com')
driver.find_element(By.XPATH, '//*[@id="passwd"]').send_keys('lamper123')
driver.find_element(By.XPATH, '//*[@id="submit_login"]').click()

time.sleep(2)

if len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/p')) != 0:
    print(len(driver.find_elements(By.XPATH, '/html/body/div[1]/div/div/div[1]')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[3]/button[1]').click()
    time.sleep(2)
if len(driver.find_elements(By.XPATH, '//*[@id="nav-sidebar"]/div/div[1]/div[4]')) != 0:
    print("wbilo do 23")
    driver.find_element(By.XPATH, '//*[@id="nav-sidebar"]/div/div[1]/div[4]/a').click()

time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="subtab-ShopParameters"]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="subtab-AdminPPreferences"]/a').click()
driver.find_element(By.XPATH, '//*[@id="general_short_description_limit"]').clear()
driver.find_element(By.XPATH, '//*[@id="general_short_description_limit"]').send_keys('3000')
driver.find_element(By.XPATH, '//*[@id="form-general-save-button"]').click()
driver.find_element(By.XPATH, '//*[@id="header_logo"]').click()

time.sleep(2)
driver.find_element(By.XPATH, '/html/body/nav/div[1]/ul/li[17]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="subtab-AdminImport"]/a').click()
driver.find_element(By.XPATH, '//*[@id="entity"]/option[1]').click()  # 1-kategorie, 2-przedmioty
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(SCIEZKA_PLIKOW+'\KATEGORIE_IMPORT.csv')

driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
if (driver.find_element(By.XPATH, '//*[@id="forceIDs_0"]').get_attribute(
        'checked') == 'true'):  # wymuś numery id ma stan 'nie'
    driver.find_element(By.XPATH,
                        '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div[4]/div/div/span').click()
if (driver.find_element(By.XPATH, '//*[@id="sendemail_1"]').get_attribute('checked') == 'true'):  # wysylaj email 'tak'
    driver.find_element(By.XPATH,
                        '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div[5]/div/div/span').click()
driver.find_element(By.XPATH,
                    '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="import"]').click()

while (driver.find_element(By.XPATH,'//*[@id="import_close_button"]').get_attribute('style')) == 'display: none;':
    time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="import_close_button"]').click()
# koniec importowania kategorii

# importowanie produktów
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="entity"]').click()
driver.find_element(By.XPATH, '//*[@id="entity"]/option[2]').click()  # 1-kategorie, 2-przedmioty
driver.find_element(By.XPATH,
                    '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[7]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(SCIEZKA_PLIKOW+'\produkty.csv')
driver.execute_script("window.scrollBy(0,500)")
if (driver.find_element(By.XPATH, '//*[@id="match_ref_0"]').get_attribute(
        'checked') == 'true'):  # uzyj indeksu jako klucza 'nie'
    driver.find_element(By.XPATH,
                        '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div[2]/div/div/span').click()
if (driver.find_element(By.XPATH, '//*[@id="forceIDs_0"]').get_attribute('checked') == 'true'):  # wymus numery id 'nie'
    driver.find_element(By.XPATH,
                        '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div[4]/div/div/span').click()
if (driver.find_element(By.XPATH, '//*[@id="sendemail_1"]').get_attribute('checked') == 'true'):  # wyslij mail 'tak'
    driver.find_element(By.XPATH,
                        '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[12]/div[5]/div/div/span').click()
driver.find_element(By.XPATH,
                    '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="type_value[4]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[4]"]/option[7]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[5]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[5]"]/option[29]').click()
driver.find_element(By.XPATH, '//*[@id="btn_right"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[6]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[6]"]/option[37]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[7]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[7]"]/option[38]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[8]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[8]"]/option[49]').click()
driver.find_element(By.XPATH, '//*[@id="import"]').click()
#zamknięcie importu produktow
while (driver.find_element(By.XPATH,'//*[@id="import_close_button"]').get_attribute('style')) == 'display: none;':
    time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="import_close_button"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="entity"]').click()
driver.find_element(By.XPATH, '//*[@id="entity"]/option[2]').click()
driver.find_element(By.XPATH, '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[1]/div[7]/button').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="file"]').send_keys(SCIEZKA_PLIKOW+'\produkty_urls.csv')

time.sleep(1)
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="main-div"]/div[2]/div[1]/div/div[2]/div/div/div[1]/form/div/div[2]/div/button').click()
driver.find_element(By.XPATH, '//*[@id="type_value[1]"]').click()
driver.find_element(By.XPATH, '//*[@id="type_value[1]"]/option[50]').click()
driver.find_element(By.XPATH, '//*[@id="import"]').click()