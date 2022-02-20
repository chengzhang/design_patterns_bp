class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class MySingletonClass(metaclass=SingletonMeta):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def some_business_logic(self):
        print(f'type: {type(self)}, id: {id(self)}, x: {self.x}, y: {self.y}')


if __name__ == '__main__':
    a = MySingletonClass(3, 7)
    a.some_business_logic()

    b = MySingletonClass(1, 2)  # 赋值不会成功
    b.some_business_logic()

