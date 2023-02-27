class LRUCache:
    __dict = None

    def __init__(self, capacity: int = 10) -> None:
        self.__dict = dict.fromkeys((range(capacity)))

    def get(self, key: str) -> str:
        return self.__dict[key]

    def set(self, key: str, value: str) -> None:
        self.__dict[key] = value
        pass

    def rem(self, key: str) -> None:
        self.__dict[key] = ''
        pass
