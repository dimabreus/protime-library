from protime import setInterval, clearInterval, setTimeout

def say_hello(name):
    print(f"Привет, {name}!")

interval = setInterval(say_hello, 1, "Дима") # Будет вызывать функцию say_hello каждую 1 секунду с параметрами "Дима".
setTimeout(clearInterval, 5, interval)
