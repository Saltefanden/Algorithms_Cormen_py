# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 13:45:58 2021

@author: nickl
"""

# Monkey patching is not available for built in types such as list (list.ins_sort = insertion_sort)
# Thus I create a subclass of list
class myList(list):
    def __init__(self, the_list):
        super().__init__(the_list)
    
    def insertion_sort(self, reverse = False):
        for i in range(1,len(self)):
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
        for i in range(len(self)):
            if self[i] == val:
                return i
        return None

    
    def selection_sort(self):
        for i in range(len(self)-1):                   # c1 * (n-1)
            minidx = i                                      # c2 * (n-2)
            minval = self[i]                                # c3 * (n-2)
            for idx, val in enumerate(self[i:]):            # c4 * sum( ti , i = 1..n-1),    ti = n-i gives n**2 running time
                if val < minval:                            # c5 * --||--   
                    minval, minidx = val, idx+i             # c6 * et eller andet hvor ofte det er sandt
            self[i], self[minidx] = minval, self[i]         # c7 * (n-2)
        return self

    @staticmethod
    def merge(arr1, arr2):
        returnlist = []
        i = j = 0
        while True:
            if i < len(arr1) and j < len(arr2):
                if arr1[i] < arr2[j]:
                    returnlist.append(arr1[i])
                    i += 1
                else:
                    returnlist.append(arr2[j])
                    j += 1
            else:
                returnlist.extend(arr1[i:] + arr2[j:])
                break
        return returnlist 

    def merge_sort(self):
        returnarray = []
        size = len(self)
        if size-1: #såfremt den ikke er hammerkort yo
            rhs = myList(self[:size//2]).merge_sort()
            lhs = myList(self[size//2:]).merge_sort()
            returnarray = myList.merge(rhs, lhs)
        else:
            returnarray = self
        return myList(returnarray)


    def bsearch_rec(self, val, enforce=False):
        #if enforce and val not in self: #is this step actually linear?!
        #    return None

        n = len(self)
        if n == 1 and enforce and val != self[0]:
            return None

        if n == 0: 
            if enforce:
                return None
            return 0 
        midpoint = self[n//2]
        returnval = False
        if val == midpoint:
            return n//2
        elif val < midpoint:
            returnval = myList(self[:n//2]).bsearch_rec(val, enforce = enforce)
        elif val > midpoint and not returnval:
            returnval = myList(self[n//2+1:]).bsearch_rec(val, enforce = enforce) 
            if returnval is not None:
                returnval += n//2 +1
        else:
            raise Exception("Logic is flawed you absolute nerd")
        return returnval


    def bsearch(self,val, enforce=False):
        """Will return the element at which the val will fit into the array, but not determine
        whether or not the element is present in the array"""
        #if enforce and val not in self: #is this step actually linear?!
        #    return None

        returnval = 0
        while True:
            n = len(self)
            if n == 1 and enforce and val != self[0]:
                return None
            if n == 0:
                if enforce:
                    return None
                return returnval
            midpoint = self[n//2]
            if val == midpoint:
                returnval += n//2
                return returnval
            elif val < midpoint:
                self = self[:n//2]
            elif val > midpoint:
                self = self[n//2 + 1: ]
                returnval += n//2+1
            else:
                raise Exception("logic flawed nerde")


    def insertion_sort_b(self):
        """Implementing insertion sort with a binary search to insert key in already sorted list.
        Assuming the list still needs to adjust elements at higher indexes when inserting, this 
        method does not ensure a Th(n lg n) running time """
        for i in range(1,len(self)):                    # ~n *
            key = self[i]
            del self[i]
            idx = myList(self[:i]).bsearch(key)             # lg n      = n lg n
            self.insert(idx, key)                           # n         = n**2            ^[1]
                                                            # [1]: https://wiki.python.org/moin/TimeComplexity
        return self


    def search_sum(self, val):
        """Finds two elements in the arr, (x, y), which sum to val: y = val - x"""
        srt_arr = self.merge_sort()                                         # n * lg n
        for i in range(len(srt_arr)):                                       # n *
            x = srt_arr[i]
            y = val - x
            # only needs to search from i and up, since x has been checked for
            # all values below by previous iterations of loop
            returnidx = myList(srt_arr[i:]).bsearch_rec(y, enforce = True)          # lg n          = n lg n
            if returnidx:
                return (x,y)
        return None
            

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
        for i in range(len(self)):
            runsum += 2**(len(self)-1 - i) * self[i]
        return runsum


# I fremtiden, sæt en testklasse op med en metode der ligner grundstrukturen i try except statements
# Dernæst lav metoder derunder der udfører testene. Hav en klassevariabel der afgør hvorvidt der skal
# udskrives kode afsluttet successfuldt. 

 
def test_Array_and_myList():
    try:
        assert myList([1,2,3,2,1,0,1]).insertion_sort() == [0,1,1,1,2,2,3], "Ins sort does not sort properly"
        assert myList([1,2,3,2,1,0,1]).insertion_sort(reverse=True) == [3,2,2,1,1,1,0], "Ins sort does not reverse sort properly"
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


def test_merge():
    try:
        assert myList.merge([1,2,3],[2,3,4]) == [1,2,2,3,3,4], "Merge malfunctions 1"
        assert myList.merge([1],[]) == [1], "Merge malfunctions 2"
        assert myList.merge([],[]) == [], "Merge malfunctions 3"
        assert myList.merge([2,4,6,8,8],[]) == [2,4,6,8,8], "Merge malfunctions 4"
        assert myList([1,2,3,2,1,0,1]).merge_sort() == [0,1,1,1,2,2,3], "Mergesort malfunction 1"
        assert myList([1]).merge_sort() == [1], "Mergesort malfunction 2"
        assert myList([1,0,0,0,0]).merge_sort() == [0,0,0,0,1], "Mergesort malfunction 3"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")    


def test_binsearch():
    try:
        testlist = myList([1,2,4,5,6,3,2,5,2,6,7,3,10,20,22,145,15,23,14,1,67,1,5,1,134,13,6,3,531,13,43,64,43,132,23,12,15,17,14])
        #print(testlist.merge_sort())
        assert testlist.merge_sort().bsearch(17) == 26, "Binsearch malfunctions 1"
        assert testlist.merge_sort().bsearch_rec(17) == 26, "Binsearch_rec malfunctions 1"
        assert testlist.merge_sort().bsearch(17,enforce = True) == 26, "Binsearch does not function with enforce on"
        assert testlist.merge_sort().bsearch_rec(17,enforce = True) == 26, "Binsearch_rec does not function with enforce on"
        assert testlist.merge_sort().bsearch(16) == 26, "bsearch does not insert nonpresent element correctly" 
        assert testlist.merge_sort().bsearch_rec(16) == 26, "bsearch_rec does not insert nonpresent element correctly" 
        assert testlist.merge_sort().bsearch(16, enforce=True) == None, "bsearch does not handle enforce property correctly" 
        assert testlist.merge_sort().bsearch_rec(16, enforce=True) == None, "bsearch_rec does not handle enforce property correctly" 
        assert myList([1,2,3]).bsearch(-210) == 0, "Bsearch does not place first element correctly"
        assert myList([1,2,3]).bsearch_rec(-210) == 0, "Bsearch_rec does not place first element correctly" 
        assert myList([1,2,3]).bsearch(210) == 3, "Bsearch does not place last element correctly" 
        assert myList([1,2,3]).bsearch_rec(210) == 3, "Bsearch_rec does not place last element correctly" 
        assert myList([]).bsearch(2) == 0, "bsearch does not handle empty arrays correctly"
        assert myList([]).bsearch_rec(2) == 0, "bsearch_rec does not handle empty arrays correctly"

    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")    


def test_insertion_sort_b():
    try:
        assert myList([1,2,3,2,1,0,1]).insertion_sort_b() == [0,1,1,1,2,2,3], "Ins sort b does not sort properly"
        assert myList([1,2,3,2,1,0,1,900,-20]).insertion_sort_b() == [-20,0,1,1,1,2,2,3,900], "Ins sort b does not sort properly"
        assert myList([-20]).insertion_sort_b() == [-20], "Ins sort b does not sort properly"
        assert myList([]).insertion_sort_b() == [], "Ins sort b does not sort properly"
    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0") 


def test_search_sum(): 
    try:
        testlist = myList([1,2,4,5,6,3,2,5,2,6,7,3,10,20,22,145,15,23,14,1,67,1,5,1,134,13,6,3,531,13,43,64,43,132,23,12,15,17,14])
        assert testlist.search_sum(132+13) == (13, 132), "Does not return the correct values if present"
        assert testlist.search_sum(-9000) == None, "Does not return None if no elements sum to val"

    except Exception as ex:
        print(ex)
    else:
        print("Code executed with return value 0")   

def main():
    # test_Array_and_myList()
    # test_binarylist()
    # test_selectionsort()
    # test_merge()
    # test_binsearch()
    # test_insertion_sort_b()
    test_search_sum()
    pass

if __name__ == '__main__':
    main()
