from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/mm43.html")
    time.sleep(1)

    # Kitöltendő mező és klikkelendő gomb
    input_field = driver.find_element_by_id("email")
    submit_button = driver.find_element_by_id("submit")

    test_data = ["teszt@elek.hu", "teszt@", ""]
    expected_error_message = ["", "Kérjük, adja meg a „@” utáni részt is. A(z) „teszt@” cím nem teljes.",
                              "Kérjük, töltse ki ezt a mezőt."] #a lokális beállítás HU nyelv, ezért a várt hibaüzenetek magyarul szerepelnek


    def email_and_click(input_data):
        """beviteli mező törlése és új adatbevitel"""
        input_field.clear()
        input_field.send_keys(input_data)
        submit_button.click()
        time.sleep(1)


    # TC1 - Helyes kitöltés
    email_and_click(test_data[0])
    error_1 = driver.find_elements_by_class_name("validation-error")
    assert len(error_1) == 0

    # TC2 - Helytelen kitöltés
    email_and_click(test_data[1])
    error_2 = driver.find_element_by_class_name("validation-error").text
    assert error_2 == expected_error_message[1]

    # TC3 - üres kitöltés
    email_and_click(test_data[2])
    error_3 = driver.find_element_by_class_name("validation-error").text
    assert error_3 == expected_error_message[2]

    time.sleep(1)

finally:
    driver.close()
