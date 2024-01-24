from threading import Timer


class RepeatedTimer:
    def __init__(self, interval, function, *args, **kwargs):
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.timer = None
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.timer = Timer(self.interval, self._run)
            self.timer.start()
            self.is_running = True

    def stop(self):
        self.timer.cancel()
        self.is_running = False


class Timeout:
    def __init__(self, timeout, function, *args, **kwargs):
        self.timeout = timeout
        self.function = function
        self.args = args
        self.kwargs = kwargs
        self.timer = None
        self.is_running = False

    def _run(self):
        self.is_running = False
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self.timer = Timer(self.timeout, self._run)
            self.timer.start()
            self.is_running = True

    def stop(self):
        self.timer.cancel()
        self.is_running = False


def setInterval(func, interval: float, *args, **kwargs):
    """
    Установка периодического выполнения функции с указанным интервалом.

    :param func: Функция, которую нужно выполнить периодически.
    :param interval: Интервал времени между вызовами функции в секундах.
    :param args: Позиционные аргументы для передачи функции.
    :param kwargs: Именованные аргументы для передачи функции.
    :return: Объект RepeatedTimer для возможности остановки периодического выполнения.
    """

    return RepeatedTimer(interval, func, *args, **kwargs)


def clearInterval(timer):
    """
    Остановка периодического выполнения функции.

    :param timer: Объект RepeatedTimer, который нужно остановить.
    """
    timer.stop()


def setTimeout(func, timeout: float, *args, **kwargs):
    """
    Установка таймаута для выполнения функции.

    :param func: Функция, которую нужно выполнить через таймаут.
    :param timeout: Время задержки в секундах.
    :param args: Позиционные аргументы для передачи функции.
    :param kwargs: Именованные аргументы для передачи функции.
    :return: Объект Timer для возможности отмены таймаута.
    """

    t = Timeout(timeout, func, *args, **kwargs)

    t.start()

    return t


def clearTimeout(timer):
    """
    Остановка таймаута выполнения функции.

    :param timer: Объект Timer, который нужно остановить.
    """
    timer.stop()
