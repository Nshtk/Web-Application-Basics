from collections import OrderedDict


class LRUCache:
    __dict = None
    __capacity = None

    def __init__(self, capacity: int = 10) -> None:
        self.__capacity = capacity
        self.__dict = OrderedDict()

    def get(self, key: str) -> str:
        if key in self.__dict:
            self.__dict.move_to_end(key)
            return self.__dict[key]
        else:
            assert key in self.__dict[key], 'Value not found'
            return ""

    def set(self, key: str, value: str) -> None:
        self.__dict[key] = value
        self.__dict.move_to_end(key)
        if len(self.__dict) > self.__capacity:
            self.__dict.popitem(last=False)

    def rem(self, key: str) -> None:
        assert key in self.__dict[key], 'Key not found'
        if key in self.__dict:
            del self.__dict[key]
