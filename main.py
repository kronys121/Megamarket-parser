import time
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import json


chrome_options = Options()

chrome_options.page_load_strategy = 'eager'

search_text = "delonghi ecam 290.31"
result_list = []

driver = uc.Chrome(options=chrome_options)


main_page = BeautifulSoup(driver.page_source, "lxml")
driver.get('https://megamarket.ru/')
# Находим элемент поиска и вставляем текст
time.sleep(4)
search_but = driver.find_element("css selector", "[class='search-tab__description-text']").click()
input_text = driver.find_element("class name", "search-input__textarea")
input_text.send_keys(search_text)
time.sleep(1)
click_but = driver.find_element("class name", "pui-button-element.pui-button-element_variant_primary.pui-button-element_size_lg")
click_but.click()
time.sleep(4)
check_boxs = driver.find_elements("class name", "filters-desktop__filter-item")


# Проверка на кол-во чек боксов и выбор Товаров в наличии
lst_elem = []
for elements in check_boxs:
    lst_elem.append(elements)
if len(lst_elem) == 3:
    available_goods = check_boxs[1]
    available_goods.click()
else:
    available_goods = check_boxs[2]
    available_goods.click()
print(len(lst_elem))
time.sleep(4)
driver.find_element("class name", "input.text-input.size").click()
elements_class = driver.find_elements("class name", "option")
element_click = elements_class[4]
element_click.click()

time.sleep(3)

titles = driver.find_elements("css selector", "[class='catalog-item-regular-desktop ddl_product catalog-item-desktop']")

for title in titles:
    bonus_price = "0%"
    bonus_amount = "0"
    name = title.find_element("css selector", "[data-test='product-name-link']").text
    price = title.find_element("css selector", "[data-test='product-price']").text
    rate = title.find_element("css selector", "[class='pui-rating-display__text-bullet']").text
    rate_count = title.find_element("css selector", "[class='pui-rating-display__narrow-text']").text

    result_list.append({
                    "Название товара": name,
                    "Цена": price,
                    "Скидка": bonus_price,
                    "Бонусные рубли": bonus_amount,
                    "Средняя оценка": rate,
                    "Кол-во комментариев": rate_count,

                })

with open("result.json","w", encoding="utf-8") as file:
    json.dump(result_list, file, indent=4, ensure_ascii=False)


time.sleep(5)