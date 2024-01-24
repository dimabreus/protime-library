from protime import setInterval, clearInterval, setTimeout

def say_hello(name):
    print(f"Привет, ${name}!")

interval = setInterval(say_hello, 1000, "Дима") # Будет вызывать функцию say_hello каждые 1000 миллисекунд с параметрами "Дима".
setTimeout(clearInterval, 5000, interval)