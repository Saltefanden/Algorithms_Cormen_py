# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:45:58 2021

@author: nickl
"""

from os import path
import random as rd

class Array:
    '''The class handles arrays and the methods on these as described in 
    the second chapter of CORMEN '''
    trainingArray = [5, 2, 4, 6, 1, 3]

    def __init__(self, array=trainingArray):
        self.array = array
        self.length = len(self.array)

    
    # Generate training data
    def random(self, length):
        self.length = length
        self.array = [rd.randrange(0,100) for i in range(length)]


    # Implement algorithms described 
    def insertion_sort(self, reverse = False):
        for i in range(1, self.length):
            key = self.array[i]
            j = i-1
            if not reverse:
                while j+1 and self.array[j] > key:
                    self.array[j+1] = self.array[j]
                    j -= 1
            else:
                while j+1 and self.array[j] < key:
                    self.array[j+1] = self.array[j]
                    j -= 1
            self.array[j+1] = key
        print(self.array)


    def search(self, v):
        for i in range(self.length):
            if self.array[i] == v:
                return i
        return None


    def merge_sort(self):
        self.array 


