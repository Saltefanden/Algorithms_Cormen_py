# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:45:58 2021

@author: nickl
"""


class ArrayToSort:

    trainingArray = [5, 2, 4, 6, 1, 3]

    def __init__(self, array=trainingArray):
        self.array = array
        self.length = len(self.array)

    def insertion_sort(self):
        for i in range(1, self.length):
            investigated_element = self.array[i]
            idx_sorted = i-1
            while idx_sorted+1 and self.array[idx_sorted] > investigated_element:
                self.array[idx_sorted+1] = self.array[idx_sorted]
                idx_sorted -= 1
            self.array[idx_sorted+1] = investigated_element
        print(self.array)


    def 