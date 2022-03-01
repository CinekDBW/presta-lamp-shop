import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("C:\Apps\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get("http://localhost:8080")
# zaawansowane
driver.find_element(By.XPATH, '//*[@id="details-button"]').click()
# otworz strone localhost (niebezpieczna)
driver.find_element(By.XPATH, '//*[@id="proceed-link"]').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# lampy podlogowe
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
# drewniane
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
# nazwa pierwszej lampy
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[1]/article/div/div[1]/h2/a').click()
# ctrl+a w ilości
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 5 w ilości
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(5)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# lampy podlogowe
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
# drewniane
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[1]/h5/a').click()
# nazwa drugiej lampy
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[2]/article/div/div[1]/h2/a').click()
# wybranie bialego koloru
driver.find_element(By.XPATH, '//*[@id="group_1"]/li[2]/label/input').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 2 w ilosc
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# nazwa pierwszego kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[1]/article/div/div[1]/h2/a').click()
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# nazwa drugiego kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[2]/article/div/div[1]/h2/a').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 2 w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# nazwa trzeciego kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[3]/article/div/div[1]/h2/a').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 3 w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(3)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# nazwa czwartego kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[4]/article/div/div[1]/h2/a').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 4 w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(2)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# nazwa piatego kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[5]/article/div/div[1]/h2/a').click()  # 5 kinkiet
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 4 w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(4)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# nazwa 6 kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[6]/article/div/div[1]/h2/a').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 5 w ilosc
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(5)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# nazwa 7 kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[7]/article/div/div[1]/h2/a').click()
# ctrl+a w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys((Keys.CONTROL, "a"))
# wpisanie 9 w ilosci
driver.find_element(By.XPATH, '//*[@id="quantity_wanted"]').send_keys(9)
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# kontynuuj zakupy
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/button').click()
# menu
driver.find_element(By.XPATH, '//*[@id="lnk-menu"]/a').click()
# kinkiety
driver.find_element(By.XPATH, '//*[@id="subcategories"]/ul/li[4]/h5/a').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# nazwa 8 kinkietu
driver.find_element(By.XPATH, '//*[@id="js-product-list"]/div[1]/div[8]/article/div/div[1]/h2/a').click()
# dodaj do koszyka
driver.find_element(By.XPATH, '//*[@id="add-to-cart-or-refresh"]/div[2]/div/div[2]/button').click()
time.sleep(3)
# przejdz do realizacji zamowienia
driver.find_element(By.XPATH, '//*[@id="blockcart-modal"]/div/div/div[2]/div/div[2]/div/div/a').click()
time.sleep(3)
# usuwanie przedmiotu
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/div[2]/ul/li[3]/div/div[3]/div/div[3]/div/a/i').click()
###
# przejdz do realizacji zamowienia, ale w podgladzie koszyka
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div[1]/div[2]/div/a').click()
# checkbox 'pan'
driver.find_element(By.XPATH, '//*[@id="field-id_gender-1"]').click()

driver.find_element(By.XPATH, '//*[@id="field-firstname"]').send_keys('Bot imie')
driver.find_element(By.XPATH, '//*[@id="field-lastname"]').send_keys('Bot nazwisko')
driver.find_element(By.XPATH, '//*[@id="field-email"]').send_keys('bot@bot.com')
driver.find_element(By.XPATH, '//*[@id="field-password"]').send_keys('lamper123')
driver.find_element(By.XPATH, '//*[@id="field-birthday"]').send_keys('1971-01-11')
# otrzymuj oferty od partnerow
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[7]/div[1]/span/label/input').click()
# przetwarzanie danych
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[8]/div[1]/span/label/input').click()
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# zapisz sie do newslettera
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[9]/div[1]/span/label/input').click()
# akceptacja regulaminu
driver.find_element(By.XPATH, '//*[@id="customer-form"]/div/div[10]/div[1]/span/label/input').click()
# dalej
driver.find_element(By.XPATH, '//*[@id="customer-form"]/footer/button').click()
try:
    if (driver.find_element(By.XPATH, '//*[@id="id-address-delivery-address-8"]/footer/a[2]').size != 0):
        driver.find_element(By.XPATH, '//*[@id="id-address-delivery-address-8"]/footer/a[2]').click()
except:
    pass

driver.find_element(By.XPATH, '//*[@id="field-address1"]').send_keys('Ul. Konwaliowa 9Z')
driver.find_element(By.XPATH, '//*[@id="field-postcode"]').send_keys('77-100')
driver.find_element(By.XPATH, '//*[@id="field-city"]').send_keys('Bytów')
# scroll okna o 500pix
driver.execute_script("window.scrollBy(0,500)")
# dalej
driver.find_element(By.XPATH, '//*[@id="delivery-address"]/div/footer/button').click()
# wybor UPS
driver.find_element(By.XPATH, '//*[@id="delivery_option_2"]').click()
time.sleep(2)
# dalej
driver.find_element(By.XPATH, '//*[@id="js-delivery"]/button').click()
# gotówka
driver.find_element(By.XPATH, '//*[@id="payment-option-2"]').click()
# zgoda na regulamin
driver.find_element(By.XPATH, '//*[@id="conditions_to_approve[terms-and-conditions]"]').click()
# skladanie zamowienia
driver.find_element(By.XPATH, '//*[@id="payment-confirmation"]/div[1]/button').click()
# klikniecie na nazwe konta
driver.find_element(By.XPATH, '//*[@id="_desktop_user_info"]/div/a[2]').click()
# historia i szczegoly zamowien
driver.find_element(By.XPATH, '//*[@id="history-link"]').click()
# szczegoly
driver.find_element(By.XPATH, '//*[@id="content"]/table/tbody/tr/td[6]/a[1]').click()
