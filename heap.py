# -*- coding: utf-8 -*-
"""
Created on Thu May  5 07:07:40 2022

@author: salman
"""


class MinHeap():
    def __init__(self, size=0):
        self.size = size
        self.members = []

    def get_left_child_index(self, arg):
        return 2*arg + 1

    def get_right_child_index(self, arg):
        return 2*arg + 2

    def get_parent_index(self, arg):
        return (arg - 1) // 2

    def has_left_child(self, arg):
        return self.get_left_child_index(arg) < self.size

    def has_right_child(self, arg):
        return self.get_right_child_index(arg) < self.size

    def has_parent(self, arg):
        return self.get_parent_index(arg) >= 0

    def left_child(self, arg):
        return self.members[self.get_left_child_index(arg)]

    def right_child(self, arg):
        return self.members[self.get_right_child_index(arg)]

    def parent(self, arg):
        return self.members[self.get_parent_index(arg)]

    def swap(self, arg1, arg2):
        temp = self.members[arg1]
        self.members[arg1] = self.members[arg2]
        self.members[arg2] = temp
        return None

    def ensure_extra_capacity(self, init_val=0, mult=2):
        self.members = self.members + [init_val]*((mult - 1)*self.size)
        return None

    def peek(self):
        if self.size == 0:
            return None
        return self.members[0]

    def poll(self):
        if self.size == 0:
            return None
        retval = self.members[0]
        self.members[0] = self.members[-1]
        self.size -= 1
        self.members = self.members[:-1]
        self.heapify_down()
        return retval

    def heapify_down(self):
        if self.size == 0:
            return None
        par_idx = 0
        while 1:
            if not (self.has_left_child(par_idx) or
                    self.has_right_child(par_idx)):
                return None
            elif not self.has_right_child(par_idx):
                if self.members[par_idx] <= self.left_child(par_idx):
                    return None
                left_idx = self.get_left_child_index(par_idx)
                self.swap(par_idx, left_idx)
                par_idx = left_idx
            else:
                if self.members[par_idx] <= self.left_child(par_idx) and\
                        self.members[par_idx] <= self.right_child(par_idx):
                    return None
                elif self.left_child(par_idx) <= self.right_child(par_idx):
                    left_idx = self.get_left_child_index(par_idx)
                    self.swap(par_idx, left_idx)
                    par_idx = left_idx
                else:
                    right_idx = self.get_right_child_index(par_idx)
                    self.swap(par_idx, right_idx)
                    par_idx = right_idx

    def heapify_up(self):
        if self.size == 0:
            return None
        child_idx = self.size - 1
        while 1:
            if not self.has_parent(child_idx):
                return None
            elif self.members[child_idx] >= self.parent(child_idx):
                return None
            else:
                par_idx = self.get_parent_index(child_idx)
                self.swap(child_idx, par_idx)
                child_idx = par_idx

    def add(self, arg):
        self.size += 1
        self.members.append(arg)
        self.heapify_up()
        return None


class MaxHeap():
    def __init__(self, size=0):
        self.size = size
        self.members = []

    def get_left_child_index(self, arg):
        return 2*arg + 1

    def get_right_child_index(self, arg):
        return 2*arg + 2

    def get_parent_index(self, arg):
        return (arg - 1) // 2

    def has_left_child(self, arg):
        return self.get_left_child_index(arg) < self.size

    def has_right_child(self, arg):
        return self.get_right_child_index(arg) < self.size

    def has_parent(self, arg):
        return self.get_parent_index(arg) >= 0

    def left_child(self, arg):
        return self.members[self.get_left_child_index(arg)]

    def right_child(self, arg):
        return self.members[self.get_right_child_index(arg)]

    def parent(self, arg):
        return self.members[self.get_parent_index(arg)]

    def swap(self, arg1, arg2):
        temp = self.members[arg1]
        self.members[arg1] = self.members[arg2]
        self.members[arg2] = temp
        return None

    def ensure_extra_capacity(self, init_val=0, mult=2):
        self.members = self.members + [init_val]*((mult - 1)*self.size)
        return None

    def peek(self):
        if self.size == 0:
            return None
        return self.members[0]

    def poll(self):
        if self.size == 0:
            return None
        retval = self.members[0]
        self.members[0] = self.members[-1]
        self.size -= 1
        self.members = self.members[:-1]
        self.heapify_down()
        return retval

    def heapify_down(self):
        if self.size == 0:
            return None
        par_idx = 0
        while 1:
            if not (self.has_left_child(par_idx) or
                    self.has_right_child(par_idx)):
                return None
            elif not self.has_right_child(par_idx):
                if self.members[par_idx] >= self.left_child(par_idx):
                    return None
                left_idx = self.get_left_child_index(par_idx)
                self.swap(par_idx, left_idx)
                par_idx = left_idx
            else:
                if self.members[par_idx] >= self.left_child(par_idx) and\
                        self.members[par_idx] >= self.right_child(par_idx):
                    return None
                elif self.left_child(par_idx) >= self.right_child(par_idx):
                    left_idx = self.get_left_child_index(par_idx)
                    self.swap(par_idx, left_idx)
                    par_idx = left_idx
                else:
                    right_idx = self.get_right_child_index(par_idx)
                    self.swap(par_idx, right_idx)
                    par_idx = right_idx

    def heapify_up(self):
        if self.size == 0:
            return None
        child_idx = self.size - 1
        while 1:
            if not self.has_parent(child_idx):
                return None
            elif self.members[child_idx] <= self.parent(child_idx):
                return None
            else:
                par_idx = self.get_parent_index(child_idx)
                self.swap(child_idx, par_idx)
                child_idx = par_idx

    def add(self, arg):
        self.size += 1
        self.members.append(arg)
        self.heapify_up()
        return None


if __name__ == '__main__':
    elements = [23, 17, 25, 10, 36, 20, 30, 42, 31, 6, 26, 11, 43, 19, 28, 34,
                22, 28, 5, 14]
    myheap = MaxHeap()
    for element in elements:
        myheap.add(element)
    for i in range(len(elements)):
        print(myheap.poll())
