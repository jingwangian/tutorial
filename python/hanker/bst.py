#!/usr/bin/env python3

# Weighted Uniform Strings

import sys


class Queue():
    def __init__(self, dlist=None):
        if dlist is not None:
            self.datalist = dlist
        else:
            self.datalist = []

    def enqueue(self, data):
        self.datalist.append(data)

    def dequeue(self):
        return self.datalist.pop(0)

    def info(self):
        return self.datalist

    def is_empty(self):
        return (len(self.datalist) == 0)


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    queue = Queue()

    def insert(self, node, data):
        if node is None:
            return Node(data)
        else:
            if data <= node.data:
                cur = self.insert(node.left, data)
                node.left = cur
            else:
                cur = self.insert(node.right, data)
                node.right = cur

        return node

    def level_order(self, root):
        if root is not None:
            self.queue.enqueue(root)

        while self.queue.is_empty() == False:
            node = self.queue.dequeue()

            print(node.data)

            if node.left is not None:
                self.queue.enqueue(node.left)
            if node.right is not None:
                self.queue.enqueue(node.right)


# T = int(input())
# mytree = Solution()
# root = None
# for i in range(T):
#     data = int(input())
#     root = mytree.insert(root, data)

def test_level_order():
    l1 = [3, 2, 5, 1, 4, 7, 20, 16, 30, 25, 12, 24]
    mytree = Solution()
    root = None
    for data in l1:
        root = mytree.insert(root, data)

    mytree.level_order(root)


test_level_order()
