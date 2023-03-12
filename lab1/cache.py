class LRUCache:
    __dict = None
    __capacity = None

    def __init__(self, capacity: int = 10) -> None:
        self.__capacity = capacity
        self.__dict = dict.fromkeys((range(capacity)))

    def get(self, key: str) -> str:
        if key in self.__dict:
            return self.__dict[key]
        else:
            assert key in self.__dict[key], 'Value not found'
            return ""

    def set(self, key: str, value: str) -> None:
        if len(self.__dict) > self.__capacity:
            self.__dict.pop(next(iter(self.__dict)))
        self.__dict[key] = value

    def rem(self, key: str) -> None:
        assert key in self.__dict[key], 'Key not found'
        if key in self.__dict:
            del self.__dict[key]
