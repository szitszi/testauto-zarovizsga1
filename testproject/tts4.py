from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/tts4.html")
    time.sleep(1)

    cf_button = driver.find_element_by_id("submit")

    # 100-szor megnyomjuk a gombot a for ciklusban és ha az eredményünk a listában vagy az épp aktuális dobásunk fej akkor növeljük a számlálót
    number_of_heads = 0
    for i in range(1, 101):
        cf_button.click()
        # result = driver.find_element_by_xpath(f'//*[@id="results"]/li[{i}]').text
        result = driver.find_element_by_id("lastResult").text
        if result == "fej":
            number_of_heads += 1
    print(number_of_heads)

    # A számlálónlnak minimum 30-nak kell lennie
    assert number_of_heads >= 30

    time.sleep(1)

finally:
    driver.close()
