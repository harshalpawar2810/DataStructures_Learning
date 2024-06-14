"""
implemented a custom list-like class in Python.

Initialization: It initializes a list with a default size of 1, and creates a Ctype array with this size.
Appending: It appends elements to the list. If the list reaches its capacity, it resizes the array to accommodate more elements.
Resizing: It doubles the capacity of the array when necessary.
Indexing: It allows indexing and slicing operations.
Popping: It removes and returns the last element of the list.
Clearing: It clears the list by resetting its size to 0 and its capacity to 1.
Finding: It finds the index of a specified value in the list.
Inserting: It inserts an element at a specified position in the list.
Removing: It removes the first occurrence of a specified value from the list.
Sorting: It sorts the list using the bubble sort algorithm.
Finding Max and Min: It finds the maximum and minimum values in the list after sorting.
Summing and Averaging: It calculates the sum and average of the elements in the list.
"""
import ctypes


class mylist:

    def __init__(self):
        self.size = 1
        self.n = 0
        # create a c type array with size = self.size
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self) -> str:
        return str(self.A[:self.n])

    def append(self, x):
        if self.n == self.size:
            self.__resize(self.size * 2)

        self.A[self.n] = x
        self.n += 1

    def __resize(self, capacity):
        B = self.__make_array(capacity)
        for k in range(self.n):
            B[k] = self.A[k]
        self.A = B
        self.size = capacity

    def __getitem__(self, i):
        if not 0 <= i < self.n:
            raise IndexError('invalid index')
        return self.A[i]

    def pop(self):
        if self.n == 0:
            raise IndexError('pop from empty list')
        print(self.A[self.n - 1])
        self.n -= 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self, x):
        for i in range(self.n):
            if self.A[i] == x:
                return i
        return "Value error not in list"

    def insert(self, i, x):
        if i < 0 or i > self.n:
            raise IndexError('invalid index')
        if self.n == self.size:
            self.__resize(2 * self.size)
        for k in range(self.n, i, -1):
            self.A[k] = self.A[k - 1]
        self.A[i] = x
        self.n += 1

    def insert(self, position, item):
        if position < 0 or position > self.n:
            raise IndexError('invalid index')
        if self.n == self.size:
            self.__resize(2 * self.size)
        for k in range(self.n, position, -1):
            self.A[k] = self.A[k - 1]
        self.A[position] = item
        self.n += 1

    def remove(self, x):
        i = self.find(x)
        if i == "Value error not in list":
            raise ValueError

    def del_item(self, i):
        if i < 0 or i > self.n:
            raise IndexError('invalid index')
        for k in range(i, self.n - 1):
            self.A[k] = self.A[k + 1]

    def __sort(self):
        # bubble_sort
        for k in range(self.n):
            for i in range(self.n - k - 1):
                if self.A[i] > self.A[i + 1]:
                    self.A[i], self.A[i + 1] = self.A[i + 1], self.A[i]

    def sort(self):
        self.__sort()

    def max(self):
        self.__sort()
        return self.A[self.n - 1]

    def min(self):
        self.__sort()
        return self.A[0]

    def sum(self):
        s = 0
        for i in range(self.n):
            s += self.A[i]
        return s

    def avg(self):
        return self.sum() / self.n

    def min(self):
        self.__sort()
        return self.A[0]

    def __make_array(self, capacity):
        # create a Ctype array(static) with size capacity
        return (capacity * ctypes.py_object)()


