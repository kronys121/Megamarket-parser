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






# content_id = content.find_all("css selector", "[class='catalog-item-regular-desktop.ddl_product catalog-item-desktop']")
#
# #Поиск и вывод элементов Цены, названия, средней оценки и кол-во комментариев
# for name_id in content_id:
#     bonus_price = "0%"
#     bonus_amount = "0"
#     try:
#         price = name_id.find("div", class_="catalog-item-regular-desktop__price-conditions").find("div",class_="catalog-item-regular-desktop__price-block").find("div", class_="catalog-item-regular-desktop__price").get_text(strip=True).replace(u'\xa0', ' ')
#         try:
#             bonus_amount = name_id.find("div", class_="catalog-item-regular-desktop__price-conditions").find("div",class_="catalog-item-regular-desktop__price-block").find("div",class_="catalog-item-regular-desktop__bonus money-bonus sm money-bonus_loyalty").find("span", class_="bonus-amount").get_text(strip=True).replace(u'\xa0', ' ')
#
#             bonus_price = name_id.find("div", class_="catalog-item-regular-desktop__price-conditions").find("div",class_="catalog-item-regular-desktop__price-block").find("div",class_="catalog-item-regular-desktop__bonus money-bonus sm money-bonus_loyalty").find("span", class_="bonus-percent").get_text(strip=True).replace(u'\xa0', ' ')
#         except AttributeError:
#             pass
#         name = name_id.find("div", class_= "catalog-item-regular-desktop__main-info").find("a").get("title").replace(u'\xa0', ' ')
#         comments_rate = name_id.find("div", class_= "catalog-item-review").find("a", class_="catalog-item-review__link").find("div", class_= "catalog-item-review__review-wrapper").find("div", class_= "pui-rating-display").find("div", class_= "pui-rating-display__rating").find("span").get_text(strip=True).replace(u'\xa0', ' ')
#         comments_rate_count = name_id.find("div", class_="catalog-item-review").find("a", class_="catalog-item-review__link").find("div", class_="catalog-item-review__review-wrapper").find("div", class_="pui-rating-display").find("div",class_="pui-rating-display__text").get_text(strip=True).replace(u'\xa0', ' ')
#         print(f"Название товара: {name} Цена: {price} Скидка: {bonus_price} Бонусные рубли: {bonus_amount} Средня оценка: {comments_rate} Кол-во комментариев: {comments_rate_count}")
#         result_list.append({
#             "Название товара": name,
#             "Цена": price,
#             "Скидка": bonus_price,
#             "Бонусные рубли": bonus_amount,
#             "Средняя оценка": comments_rate,
#             "Кол-во комментариев": comments_rate_count,
#
#         })
#     except AttributeError:
#         pass
#
# with open("result.json","w", encoding="utf-8") as file:
#     json.dump(result_list, file, indent=4, ensure_ascii=False)


time.sleep(5000)