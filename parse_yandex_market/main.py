from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get("https://market.yandex.kz/catalog--usb-flash-drive/54529/list?hid=288003&glfilter=5059792%3A12834683%2C12107033&glfilter=5059793%3A32~32&onstock=1&local-offers-first=0&how=quality&page=1")
    items = browser.find_elements_by_css_selector(
        "n-snippet-card2 i-bem b-zone b-spy-visible b-spy-visible_js_inited b-zone_js_inited n-snippet-card2_js_inited")
    for item in items:
        print(item)
        name = item.find_element_by_css_selector(
            "div.n-snippet-card2__part_type_center a.n-link_theme_blue")
        print(name.text)
