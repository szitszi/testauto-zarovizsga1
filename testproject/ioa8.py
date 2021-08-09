from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/ioa8.html")
    time.sleep(1)

    # Kikeressük az egyes számokat illetve a műveleti jelet, majd kalkulálunk
    first_number = int(driver.find_element_by_id("num1").text)
    operator_character = driver.find_element_by_id("op").text
    second_number = int(driver.find_element_by_id("num2").text)
    calc_button = driver.find_element_by_id("submit")
    calc_button.click()
    time.sleep(1)

    # Az alkalmazás által számolt eredményt összehasonlítjuk a saját számításunkkal
    calculated_result_by_app = int(driver.find_element_by_id("result").text)

    # A saját számításunkhoz az app számait és műveleti jeleit használjuk, azért alkalmazunk elágazást, mert a műveleti jelet ilyen formában lehet csak megfogni
    if operator_character == "+":
        assert calculated_result_by_app == (first_number + second_number)
        print(first_number + second_number)
    elif operator_character == "-":
        assert calculated_result_by_app == (first_number - second_number)
        print(first_number - second_number)
    elif operator_character == "*":
        assert calculated_result_by_app == (first_number * second_number)
        print(first_number * second_number)
    else:
        assert calculated_result_by_app == (first_number / second_number)
        print(first_number / second_number)

    print(calculated_result_by_app)

    time.sleep(1)

finally:
    driver.close()
