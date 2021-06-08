class Demo:
    def __init__(self):
        self.__data = {}

    def __str__(self):
        return str(self.__data)

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __getitem__(self, item):
        return self.__data.get(item)


if __name__ == '__main__':
    d = Demo()
    print(d)
    d["A"] = "test"
    print(d)
    print(d['A'])
    print(d['bb'])
