- входные данные
- тестовый сценарий, то есть набор шагов, которые надо выполнить для получения результата
- проверка ожидаемого результата


- pytest -v (verbose: подробный отчет) файл/директория
- -s (show: выводит out функции print())

## INFO
Если нам нужно проверить, что тест вызывает ожидаемое исключение 
(что довольно редкая ситуация для UI-тестов, и вам это способ 
скорее всего никогда не пригодится), то мы можем использовать 
специальную конструкцию with pytest.raises(). Например, можно 
проверить, что на странице сайта не должен отображаться какой-то 
элемент:

```
from selenium import webdriver
browser = webdriver.Chrome()
def test_exception():
    browser.get("https://mysite.com")
    with pytest.raises(NoSuchElementException, message="Не должно быть кнопки Отправить"):
        browser.find_element_by_css_selector("button.btn")
```

## Fixture
Фикстуры представляют из себя сервисы для конструкторы и
деструкторы в приложении для тестирования
> пример: test_fixture.py
>  def setup_method(self): # конструктор
> def teardown_method(self): # деструктор

