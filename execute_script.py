from selenium import webdriver

browser = webdriver.Chrome()

browser.get("https://try.jsoup.org/")

browser.execute_script("document.title='hell';alert('sup');")
