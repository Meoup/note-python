class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


class A(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    a = A('1')
    print(id(a))
    print(a.name)
    b = A('2')
    print(id(b))
    print(b.name)
