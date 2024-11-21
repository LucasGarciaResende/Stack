from typing import Any


class Stack:

    def __init__(self) -> None:
        self._stack: list[Any] = []

    def _type_check(self, obj_to_check: list | set | tuple) -> None:
        if not isinstance(obj_to_check, (list, set, tuple)):
            raise TypeError(f"Invalid data type of {obj_to_check}: {type(obj_to_check)}\n"
                            "Must be of: List, Set or Tuple.")

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
        self._int_check(amount)
        if amount:
            self.stack(self.stack()[:-amount])
        else:
            self.stack().pop()
