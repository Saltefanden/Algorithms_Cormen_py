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


# Monkey patching is not available for built in types such as list (list.ins_sort = insertion_sort)
# Thus I create a subclass of list
class myList(list):
    def __init__(self, the_list):
        super().__init__(the_list)
    
    def insertion_sort(self, reverse = False):
        for i in range(1,self.__len__()):
            key = self[i]
            j = i-1
            if not reverse:
                while j>=0 and self[j]>key:
                    self[j+1] = self[j]
                    j -= 1
            else:
                while j>=0 and self[j]<key:
                    self[j+1] = self[j]
                    j -= 1
            self[j+1] = key
        return self
    
    def search(self, val):
        """Searches for a value in the array, if the value is present, return the index"""
        for i in range(self.__len__()):
            if self[i] == val:
                return i
        return None

    
    def selection_sort(self):
        for i in range(self.__len__()-1):                   # c1 * (n-1)
            minidx = i                                      # c2 * (n-2)
            minval = self[i]                                # c3 * (n-2)
            for idx, val in enumerate(self[i:]):            # c4 * sum( ti , i = 1..n-1),    ti = n-i gives n**2 running time
                if val < minval:                            # c5 * --||--   
                    minval, minidx = val, idx+i             # c6 * et eller andet hvor ofte det er sandt
            self[i], self[minidx] = minval, self[i]         # c7 * (n-2)
        return self


class binarylist(list):
    def __init__(self, *args):
        super().__init__([*args])
        for i in range(len(args)):
            if self[i] not in [0,1]:
                raise ValueError("Element {} not binary".format(i))
    
    @staticmethod
    def _add_element(x,y):
        return int((x or y) and not (x and y))
    
    @staticmethod
    def _carry_over(x,y):
        return int(x and y)
    
    def __add__(self, other):
        if self.__len__() >= other.__len__():
            longest = self
            shortest = other
        else:
            longest = other
            shortest = self

        #New array is at most one longer than the longest
        resultsize = longest.__len__() +1
        resultarray = [0 for i in range(resultsize)]
        carry = 0
        for i in range(1,resultsize):
            if i <= shortest.__len__(): 
                # Add two elements, no carry considered
                temp_carry = binarylist._carry_over(self[-i], other[-i])
                resultarray[-i] = binarylist._add_element(self[-i], other[-i])
                # Finally add the carry and update next carry
                resultarray[-i], carry = binarylist._add_element(resultarray[-i], carry), binarylist._carry_over(resultarray[-i], carry) + temp_carry
                assert carry < 2, "Miscalculated carry"
            else: 
                resultarray[-i], carry = binarylist._add_element(longest[-i], carry), 0
        return binarylist(*resultarray)
    
    def parse(self):
        runsum = 0 
        for i in range(self.__len__()):
            runsum += 2**(self.__len__()-1 - i) * self[i]
        return runsum
            

    

def test_Array_and_myList():
    try:
        assert Array([2,3,1,4,5]).insertion_sort() == [1,2,3,4,5], "Ins sort does not sort properly"
        assert Array([2,3,1,4,5]).insertion_sort(reverse = True) == [5,4,3,2,1], "Ins sort does not reverse sort properly"
        assert Array([2,3,1,4,5]).search(4) == 3, "Search does not search properly"
        assert myList([1,2,3,2,1,0,1]).insertion_sort() == [0,1,1,1,2,2,3], "Ins sort does not sort properly"
        assert myList([1,2,3,2,1,0,1]).insertion_sort(reverse=True) == [3,2,2,1,1,1,0], "Ins sort does not reverse sort properly"
        assert myList([1,0]).insertion_sort() == [0,1], "Ins sort does not sort properly"
        assert myList([0,0]).insertion_sort() == [0,0], "Ins sort does not sort properly"
        assert myList([0,1,2,3,4,5,-6,7,8]).search(-6) == 6, "Search does not return proper index"
        assert myList([0,1,2,3,4,5,-6,7,8]).search(-61) == None, "Search does not return None if value not present"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")


def test_binarylist():
    try:
        assert binarylist(1,1,1,1,1).parse() == 31, "Parsing wrong"
        assert binarylist(1,1,1,0,1).parse() == 29, "Parsing wrong"
        lol = binarylist(1,0,1,0)
        lol1 = binarylist(1,0,0,0,0,0,1)
        lol2 = lol + lol1
        assert lol2.parse() == lol.parse() + lol1.parse(), "Adding wrong"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")


def test_selectionsort():
    try:
        assert myList([1,2,3,2,1,0,1]).selection_sort() == [0,1,1,1,2,2,3], "Sel sort does not sort properly"
        assert myList([1,2,3,2,1,0,1,0]).selection_sort() == [0,0,1,1,1,2,2,3], "Sel sort does not sort properly"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")



def main():
    test_selectionsort()

if __name__ == '__main__':
    main()
