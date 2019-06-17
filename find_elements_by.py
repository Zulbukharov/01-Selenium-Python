from selenium import webdriver

browser = webdriver.Chrome()
# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
browser.get("http://suninjuly.github.io/huge_form.html")

elements = browser.find_elements_by_xpath("//input")
for element in elements:
    element.send_keys("yay")

button = browser.find_element_by_css_selector("button.btn")
button.click()

# # добавляем товар в корзину
# add_button = browser.find_element_by_css_selector(".add")
# add_button.click()

# # открываем страницу второго товара
# browser.get("https://fake-shop.com/book2.html")

# # добавляем товар в корзину
# add_button = browser.find_element_by_css_selector(".add")
# add_button.click()

# # тестовый сценарий
# # открываем корзину
# browser.get("https://fake-shop.com/basket.html")

# # ищем все добавленные товары
# goods = browser.find_elements_by_css_selector(".good")

# # проверяем, что количество товаров равно 2
# assert len(goods) == 2
