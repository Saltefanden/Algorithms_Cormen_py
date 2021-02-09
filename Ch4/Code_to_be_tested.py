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
        if size>1: #såfremt den ikke er hammerkort yo
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

