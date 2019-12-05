class Array:

    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __getitem__(self, position: int) -> object:
        return self._data[position]

    def __len__(self) -> int:
        return len(self._data)

    def __setitem__(self, index: int, value: object):
        self._data[index] = value

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

if __name__ == "__main__":
    array = Array(5)
    array.insert(0,1)
    print(array[0])
    array[0] = 5
    print(array[0])
    print('ttttttttest revert')



