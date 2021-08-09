from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/x234.html")
    time.sleep(1)

    # Használanó mezők és gomb
    a_field = driver.find_element_by_id("a")
    b_field = driver.find_element_by_id("b")
    calc_button = driver.find_element_by_id("submit")

    # Tesztadatok listába gyűjtve
    data_for_a = ["99", "kiskutya", ""]
    data_for_b = ["12", "12", ""]
    expected_result = ["222", "NaN", "NaN"]


    # Függvény megadása, ahol a három teszteset azonos lépései szerepelnek
    def send_and_calc(input_a, input_b, exp_result):
        a_field.clear()
        b_field.clear()
        a_field.send_keys(input_a)
        b_field.send_keys(input_b)
        calc_button.click()
        received_result = driver.find_element_by_id("result").text
        assert received_result == exp_result
        print(received_result)


    # A három különböző teszteset egy for ciklusban tesztelhető, ahol a 0. indexhez az 1. teszeset tartozik, és így tovább
    for i in range(3):
        send_and_calc(data_for_a[i], data_for_b[i], expected_result[i])

    time.sleep(1)

finally:
    driver.close()