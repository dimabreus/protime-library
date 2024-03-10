# protime-library

## Python библиотека для облегчения работы с интервалами.

### Использование:
1. Скачать файл `protime.py`;
2. Переместить файл в одну из директорий где Python ищет библиотеки;
3. Импортировать библиотеку в используемом коде.

### Как посмотреть директории где python ищет библиотеки:
```python
import sys

print(sys.path)
```

### Как добавить новую директорию:
1. Откройте командную строку с правами администратора;
2. Напишите следующий код:
```bash
SET PYTHONPATH=Ваш путь
```
3. Перезапустите пк.

### Пример использования:
```python
from protime import setInterval, clearInterval, setTimeout

def say_hello(name):
    print(f"Привет, {name}!")

interval = setInterval(say_hello, 1, "Дима") # Будет вызывать функцию say_hello каждые 1000 миллисекунд с параметрами "Дима".
setTimeout(clearInterval, 5, interval)
```
#### Output:
[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=16&duration=1000&pause=1000&color=ACB6F7&multiline=true&random=false&width=435&height=125&lines=%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%2C+%D0%94%D0%B8%D0%BC%D0%B0!;%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%2C+%D0%94%D0%B8%D0%BC%D0%B0!;%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%2C+%D0%94%D0%B8%D0%BC%D0%B0!;%D0%9F%D1%80%D0%B8%D0%B2%D0%B5%D1%82%2C+%D0%94%D0%B8%D0%BC%D0%B0!)](https://git.io/typing-svg)
