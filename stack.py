#coding: utf-8

from typing import Any

class Stack:

    def __init__(self):
        self.__content = []
        self.__size = 0

    def __bool__(self) -> bool:
        return self.__size != 0

    def __len__(self) -> int:
        return self.__size

    def push(self, element:Any) -> None:
        self.__content.append(element)
        self.__size += 1

    def pop(self) -> Any:
        self.__size -= 1
        return self.__content.pop()

    def seek(self) -> Any:
        return self.__content[-1]