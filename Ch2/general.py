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
        return self.array


    def search(self, v):
        for i in range(self.length):
            if self.array[i] == v:
                return i
        return None


    def merge_sort(self):
        self.array 

# Monkey patching is not available for built in types such as list (list.ins_sort = insertion_sort)
# Thus I create a subclass of list
class myList(list):
    def __init__(self, the_list):
        super().__init__(the_list)
    
    def insertion_sort(self):
        for i in range(1,self.__len__()):
            key = self[i]
            j = i-1
            while j>=0:
                if self[j] > key:
                    self[j+1] = self[j]
                    self[j] = key
                    j -= 1
                else:
                    self[j+1] = key
                    break
        return self




def main():
    try:
        assert Array([2,3,1,4,5]).insertion_sort() == [1,2,3,4,5], "Ins sort does not sort properly"
        assert Array([2,3,1,4,5]).insertion_sort(reverse = True) == [5,4,3,2,1], "Ins sort does not reverse sort properly"
        assert Array([2,3,1,4,5]).search(4) == 3, "Search does not search properly"
        assert myList([1,2,3,2,1,0,1]).insertion_sort() == [0,1,1,1,2,2,3], "Ins sort does not sort properly"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")
    

if __name__ == '__main__':
    main()
