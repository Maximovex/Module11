import inspect


def introspection_obj(obj):
    print('Тип обьекта: ', type(obj))
    attr_lst = []
    method_lst = []
    filtered=[x for x in dir(obj) if not x.startswith('__')]
    for attr in filtered:
        if not callable(getattr(obj, attr)):
            attr_lst.append(attr)
        else:
            method_lst.append(attr)

    print(f'Аттрибуты объекта {obj}:\n {attr_lst}')
    print(f'Методы объекта {obj}:\n {method_lst}')
    print(f'Модуль объекта {obj}: {inspect.getmodule(obj)}')


class Some_class:
    def __init__(self):
        self.some_attr = None

    def hello(self):
        print('Hello')

    def hello2(self):
        print('Hello2')


introspection_obj(42)
introspection_obj(Some_class)
