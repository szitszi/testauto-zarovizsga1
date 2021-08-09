from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

opt = Options()
opt.headless = False

driver = webdriver.Chrome(ChromeDriverManager().install(), options=opt)
driver.set_window_rect(1200, 400, 1300, 1000)

try:
    driver.get("https://black-moss-0a0440e03.azurestaticapps.net/rv4.html")
    time.sleep(1)

    missing_city_field = driver.find_element_by_id("missingCity")
    check_button = driver.find_element_by_id("submit")
    result_message = driver.find_element_by_id("result")

    cites = driver.find_element_by_id("cites").get_attribute("value")
    print(cites)
    print(type(cites))

    city_list = cites.replace('"', '').split(", ")
    print(city_list)
    city_list.sort()
    print(city_list)

    list_with_gap = driver.find_elements_by_xpath('//*[@id="randomCities"]/li')
    list_with_missing_city = []
    for town in list_with_gap:
        list_with_missing_city.append(town.text)
    list_with_missing_city.sort()
    print(list_with_missing_city)

    for i in range(len(list_with_missing_city)):
        if city_list[i] == list_with_missing_city[i]:
            pass
        else:
            print("The missing city is: ")
            print(city_list[i])
            missing_town = city_list[i]

            missing_city_field.send_keys(missing_town)
            check_button.click()
            break

    assert result_message.text == "Eltaláltad."

    time.sleep(3)

finally:
    driver.close()
