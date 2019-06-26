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

> def setup_method(self): # конструктор

> def teardown_method(self): # деструктор

## Marks
Есть приоритеты
- проверка после каждого коммита
> @pytest.mark.smoke
- проверка перед деплоем
> @pytest.mark.regression
- пропуск
> @pytest.mark.skip
- для падающего
> @pytest.mark.xfail


Для запуска опредленных используется флаг -m
> pytest -m smoke test_file.py

inversion
> pytest -m 'not smoke' test_file.py

or
> pytest -m "smoke or regression" test_file.py

parametres
> @pytest.mark.parametrize('language', ["ru", "en-gb"])


