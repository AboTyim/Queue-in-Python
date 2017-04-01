#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
# © 2017 Syrian Programmer.
#
# Queue FIFO: First In, First Out
#
# Coded in Date: 30/3/2017.
#


class Queue:
    """ Python implementation the queue """

    def __init__(self, items=None):
        if items is None:
            items = []
        self.__items = items

    def enqueue(self, item):
        self.__items.append(item)

    def dequeue(self):
        return self.__items.pop(0)

    def peek(self):
        return self.__items[0]

    def clear(self):
        self.__items.clear()

    def is_empty(self):
        return self.__items == []

    def get_items(self):
        return self.__items

    def size(self):
        return len(self.__items)

    def __len__(self):
        return len(self.__items)

    def __getitem__(self, item):
        return self.__items[item]


# Sample inputs
if __name__ == '__main__':
    x = [10, 20, 30, 40, 50, 60]

    q = Queue(x)
    q.enqueue(70)
    q.enqueue(80)
    print(q.get_items())

    print(q.dequeue())
    print(q.dequeue())
    print(q.get_items())

    print(len(q))
    print(q.size())
    print(q.is_empty())
    print(q.get_items())

    q.clear()
    print(q.get_items())

    q.enqueue(70)
    q.enqueue(80)
    print(q.get_items())

    print(q.dequeue())
    print(q.peek())
    print(q.get_items())
    print(q[-1])

