import time
import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
import json
from loguru import logger

class MMParser:

    def __init__(self, input_text: str,):
        self.input_text = input_text
        self.data = []

    def browser_settings(self):
        chrome_options = Options()
        chrome_options.page_load_strategy = 'eager'
        self.driver = uc.Chrome(options=chrome_options)
        self.driver.get('https://megamarket.ru/')

    def search_put(self):
        time.sleep(4)
        self.driver.find_element("css selector", "[class='search-tab__description-text']").click()
        self.driver.find_element("class name", "search-input__textarea").send_keys(self.input_text)
        time.sleep(1)
        click_but = self.driver.find_element("class name",
                                        "pui-button-element.pui-button-element_variant_primary.pui-button-element_size_lg")
        click_but.click()
        time.sleep(4)

    def param(self):
        check_boxs = self.driver.find_elements("class name", "filter-title.filters-desktop__solo-title-text")

        lst_elem = []
        for elements in check_boxs:
            lst_elem.append(elements.text)

        index_box_available = lst_elem.index("В наличии")
        check_boxs[index_box_available].click()
        time.sleep(4)
        self.driver.find_element("class name", "input.text-input.size").click()
        elements_class = self.driver.find_elements("class name", "option")
        elements_class[4].click()
        time.sleep(4)

    def pars_data(self):
        titles = self.driver.find_elements("css selector",
                                      "[class='catalog-item-regular-desktop ddl_product catalog-item-desktop']")

        for title in titles:
            bonus_price = "0%"
            bonus_amount = "0"
            name = title.find_element("css selector", "[data-test='product-name-link']").text
            price = title.find_element("css selector", "[data-test='product-price']").text
            rate = title.find_element("css selector", "[class='pui-rating-display__narrow-text']").text
            rate_count = title.find_element("css selector", "[class='pui-rating-display__text']").text.strip("\n•")

            data = {"Название товара": name,
                    "Цена": price,
                    "Скидка": bonus_price,
                    "Бонусные рубли": bonus_amount,
                    "Средняя оценка": rate,
                    "Кол-во комментариев": rate_count,}
            logger.add("debug.log", format="{time} {level} {message}",)
            logger.info(f'Добавил: {name}, {price}, {rate}')
            self.data.append(data)
        self.save_data()




    def save_data(self):
        with open("result.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

        self.driver.quit()

    def start_pars(self):
        self.browser_settings()
        self.search_put()
        self.param()
        self.pars_data()

if __name__ == "__main__":
    MMParser(input_text="delonghi ecam 290.31").start_pars()

