import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
s = Service("C:\Program Files\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("http://localhost:8080")

driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[1]/article/div/a/img').click()#pierwsza lampa drewniana
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(5)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/div/a/img').click()
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[1]/article/div/a/img').click()#druga lampa drewniana
driver.find_element(By.XPATH, '//*[@id="group_1"]/li[2]/label/input').click()
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[1]/article/div/a/img').click()#pierwszy kinkiet
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[2]/article/div/a/img').click()#drugi kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[3]/article/div/a/img').click()#trzeci kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(3)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[4]/article/div/a/img').click()#czwarty kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[5]/article/div/a/img').click()#5 kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(4)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[6]/article/div/a/img').click()#6 kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(5)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[7]/article/div/a/img').click()#7 kinkiet
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(9)
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/div/a/img').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[8]/article/div/a/img').click()#8 kinkiet
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/a').click()
time.sleep(2)
#usuwanie przedmiotu
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/ul/li[3]/div/div[3]/div/div[3]/div/a/i').click()
###
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a').click()
driver.find_element(By.XPATH, '//*[@id="field-id_gender-1"]').click()
driver.find_element(By.XPATH, '//*[@id="field-firstname"]').send_keys('Bot imie')
driver.find_element(By.XPATH, '//*[@id="field-lastname"]').send_keys('Bot nazwisko')
driver.find_element(By.XPATH, '//*[@id="field-email"]').send_keys('bot@bot.com')
driver.find_element(By.XPATH, '//*[@id="field-password"]').send_keys('lamper123')
driver.find_element(By.XPATH, '//*[@id="field-birthday"]').send_keys('1971-01-11')
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[7]/div[1]/span/label/input').click()
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[8]/div[1]/span/label/input').click()
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[9]/div[1]/span/label/input').click()
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[10]/div[1]/span/label/input').click()
driver.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button').click()
driver.find_element(By.XPATH, '//*[@id="field-address1"]').send_keys('Ul. Konwaliowa 9Z')
driver.find_element(By.XPATH, '//*[@id="field-postcode"]').send_keys('77-100')
driver.find_element(By.XPATH, '//*[@id="field-city"]').send_keys('Bytów')
driver.execute_script("window.scrollBy(0,500)")
driver.find_element(By.XPATH, '//*[@id="delivery-address"]/div/footer/button').click()
driver.find_element(By.XPATH, '//*[@id="delivery_option_2"]').click()
driver.find_element(By.XPATH, '//*[@id="js-delivery"]/button').click()
driver.find_element(By.XPATH, '//*[@id="payment-option-2"]').click()
driver.find_element(By.XPATH, '//*[@id="conditions_to_approve[terms-and-conditions]"]').click()
driver.find_element(By.XPATH, '//*[@id="payment-confirmation"]/div[1]/button').click()
driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]/div/a[2]').click()
driver.find_element(By.XPATH, '//*[@id="history-link"]').click()
driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr/td[6]/a[1]').click()






