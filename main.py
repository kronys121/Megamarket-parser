import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

chrome_options = Options()

chrome_options.page_load_strategy = 'eager'
chrome_options.add_argument("--window-size=1920,1080")

search_text = "delonghi"

def stealth_driver():
    browser = webdriver.Chrome(options=chrome_options)
    stealth(browser,
            platform='win32',
            languages=['en-US', 'en'],
            vendor='Google Inc.',
            )

    return browser

driver = stealth_driver()
driver.get('https://megamarket.ru/')

time.sleep(4)
search_but = driver.find_element(By.CLASS_NAME, 'search-tab')
search_but.click()
input_text = driver.find_element("class name", "search-input__textarea")
input_text.send_keys(search_text)
time.sleep(1)
click_but = driver.find_element("class name", "pui-button-element.pui-button-element_variant_primary.pui-button-element_size_lg")
click_but.click()
time.sleep(4)
check_boxs = driver.find_elements("class name", "pui-checked-control-item__label.pui-toggle__label")

lst_elem = []
for elements in check_boxs:
    lst_elem.append(elements)
if len(lst_elem) == 6:
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

time.sleep(6)

main_page = BeautifulSoup(driver.page_source, "lxml")

content = main_page.find("div",class_="catalog-items-list__container")

content_id = content.find_all("div", class_="catalog-item-regular-desktop")
for name_id in content_id:
    try:
        price = name_id.find("div", class_="catalog-item-regular-desktop__price-conditions").find("div",class_="catalog-item-regular-desktop__price-block").find("div", class_="catalog-item-regular-desktop__price").get_text(strip=True)
        name = name_id.find("div", class_= "catalog-item-regular-desktop__main-info").find("a").get("title")
        comments_rate = name_id.find("div", class_= "catalog-item-review").find("a", class_="catalog-item-review__link").find("div", class_= "catalog-item-review__review-wrapper").find("div", class_= "pui-rating-display").find("div", class_= "pui-rating-display__rating").find("span").get_text(strip=True)
        comments_rate_count = name_id.find("div", class_="catalog-item-review").find("a", class_="catalog-item-review__link").find("div", class_="catalog-item-review__review-wrapper").find("div", class_="pui-rating-display").find("div",class_="pui-rating-display__text").get_text(strip=True)
        print(f"Название товара: {name} Цена: {price} Средня оценка: {comments_rate} Кол-во комментариев: {comments_rate_count}")
    except AttributeError:
        print("Скорее всего товара нет в наличии")









time.sleep(50)