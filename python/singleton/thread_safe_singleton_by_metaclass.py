from threading import Lock, Thread


class ThreadSafeSingletonMeta(type):
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class MySingletonClass(metaclass=ThreadSafeSingletonMeta):
    value: str = None

    def __init__(self, value):
        self.value = value

    def some_business_logic(self):
        print(f'type: {type(self)}, id: {id(self)}, value: {self.value}')


def thread_func(value: str):
    obj = MySingletonClass(value)
    obj.some_business_logic()


if __name__ == '__main__':
    thd1 = Thread(target=thread_func, args=('foo', ))
    thd2 = Thread(target=thread_func, args=('bar', ))
    thd1.start()
    thd2.start()
