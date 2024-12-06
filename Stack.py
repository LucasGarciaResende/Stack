"""
Stack

A class that creates and manages a custom Stack data structure (LI-FO Last-in-First-out).

Private Attributes:
    _stack (list[Any]): Stores the list that represents the stack.

Methods:
    __init__():
        Initializes with an empty stack.

    __eq__() -> bool:
        Returns True or False if the stack in two Stack objects are equal or not respectively.

    __or__(self, other):
        Returns a new Stack object by concatenating the stacks of two different Stack objects.

    _type_check(obj_to_check: list | set | tuple) -> None:
        Checks if an object is of type list, set or tuple
        Throws a TypeError exception if False

    _int_check(self, obj_to_check: int) -> None:
        Checks if a value is of type int, then checks if the value is bigger than the length of the stack.
        Throws a TypeError if not an int or a ValueError if the value is bigger than the length

    stack(self, stack: list | set | tuple = None) -> None | list[Any]:
        Takes a list, set or tuple and sets it as the stack.
        Returns the stack if there's no input.

    add(self, item: Any) -> None:
        Adds any value to the top of the stack.

    remove(self, amount: int = None) -> None:
        Receives an integer i and removes i items from the top of the stack.
        If there's no input removes only the first item at the top of the stack.
"""

from typing import Any


class Stack:

    def __init__(self) -> None:
        self._stack: list[Any] = []

    def __eq__(self, other) -> bool:
        return self.stack() == other.stack()

    def __or__(self, other):
        return self.stack() + other.stack()

    @staticmethod
    def _type_check(obj_to_check: list | set | tuple) -> None:
        if not isinstance(obj_to_check, (list, set, tuple)):
            raise TypeError(f"Invalid data type of {obj_to_check}: {type(obj_to_check)}\n"
                            "Must be of type: List, Set or Tuple.")

    def _int_check(self, obj_to_check: int) -> None:
        if not isinstance(obj_to_check, int):
            raise TypeError(f"Invalid data type of {obj_to_check}: {type(obj_to_check)}, must be an Integer.")
        if obj_to_check > len(self.stack()):
            raise ValueError(f"Value exceeds the length of the stack.")

    def stack(self, stack: list | set | tuple = None) -> None | list[Any]:
        if stack:
            self._type_check(stack)
            self._stack = stack
        else:
            return self._stack

    def add(self, item: Any) -> None:
        self.stack().append(item)

    def remove(self, amount: int = None) -> None:
        if amount:
            self._int_check(amount)
            self.stack(self.stack()[:-amount])
        else:
            self.stack().pop()


#Main method for testing purposes
def main() -> None:
    # Creating Stack objects.
    teststack: Stack = Stack()
    teststack2: Stack = Stack()

    # Adding a Stack to the object.
    teststack.stack([1, 2, 3])
    teststack2.stack([4, 5, 6])

    # Printing the Results.
    print(teststack.stack())
    print(teststack | teststack2)
    print(teststack == teststack2)
    teststack2.stack([1, 2, 3])
    print(teststack == teststack2)

    #Testing the Remove and add methods
    teststack.remove()
    print(teststack.stack())
    teststack2.remove(2)
    print(teststack2.stack())
    teststack.add(3)
    print(teststack.stack())
    teststack2.add(2)
    teststack2.add(3)
    print(teststack2.stack())

    #Testing exceptions
    # teststack.remove('a')
    # teststack.stack(3)
    # teststack.remove(4)

if __name__ == '__main__':
    main()
