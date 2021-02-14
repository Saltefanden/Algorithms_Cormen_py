# INTET AF FØLGENDE VIRKER
# print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
# from Ch2 import general as g 
# print(g.myList([2,3,5,1,3,6,23,0,-12,1,4,2,5]).merge_sort())
# print("We did it boissss")
# from ..Ch2.general import myList
# print('lol')


#%% Virker sgu nærmest heller ikke
# import sys

# sys.path.append('./Ch2')
# from general import myList 

# # Herfra kan vi monkey patche myList. 
# # Ydermere fucking pytest virker ikke hvis der er en __init__ fil i samme mappe..... omfg https://stackoverflow.com/questions/41748464/pytest-cannot-import-module-while-python-can

# def addone(my_list):
#     returnlist = []
#     for i, val in enumerate(my_list):
#         returnlist.append(val +1) 
#     return returnlist

# myList.addone = addone 


# if __name__ == '__main__':
#     lol = myList([1,2,3])
#     lol = lol.addone()
#     print(lol)

#%%  Det her virker til gengæld på pytest også, så det er muligt at lave monkey patchede tests uden at gøre mere for det. 
# from Code_to_be_tested import myList

# def addone(my_list):
#     returnlist = []
#     for i, val in enumerate(my_list):
#         returnlist.append(val +1) 
#     return returnlist

# myList.addone = addone 


# %% Det her er samlet set bedst? Vi har nu fjernet alle tomme __init__ filer som pytest ikke kan lide og som heller ikke gør nogen forskel siden python 3.x tidligt
# For fremtidige moduler der skal bruge denne funktion: https://stackoverflow.com/questions/19545982/monkey-patching-a-class-in-another-module-in-python
import sys

sys.path.insert(1,'../Ch2')

from general import myList 

def addone(my_list):
    returnlist = []
    for i, val in enumerate(my_list):
        returnlist.append(val +1) 
    return returnlist

myList.addone = addone 

def largest_cross_array(my_list, start, mid, stop):
    sum = 0
    leftsum, rightsum = None, None
    for i in range(mid-1, start-1, -1): # mid-1
        sum += my_list[i]
        if leftsum is None or sum > leftsum:
            leftsum = sum
            startidx = i
    if leftsum is None:
        leftsum = 0 
        startidx = mid
    sum = 0
    for i in range(mid,stop):
        sum += my_list[i]
        if rightsum is None or sum > rightsum:
            rightsum = sum
            stopidx = i+1 #As a range will have to give the end of range value. 
    if rightsum is None:
        rightsum = 0
        startidx = mid
    return leftsum + rightsum, startidx, stopidx


def largest_sublist(my_list, start=0, stop=None):
    if stop is None:
        stop = len(my_list)
    if stop == 0:
        return (None, None, None)
    if start == stop-1:
        return my_list[start], start, stop
    mid = (stop + start) //2
    #Either the largest sublist is to the left
    sumleft, startleft, stopleft = largest_sublist(my_list, start=start, stop=mid)
    #or the right
    sumright, startright, stopright = largest_sublist(my_list,start=mid, stop=stop)
    #or cross the middle
    crosssum, startcross, stopcross = largest_cross_array(my_list, start=start, stop=stop, mid=mid)
    if sumleft >= sumright and sumleft >= crosssum:
        return sumleft, startleft, stopleft   
    if crosssum >= sumleft and crosssum >= sumright:
        return crosssum, startcross, stopcross
    if sumright >= sumleft and crosssum <= sumright:
        return sumright, startright, stopright


#myList.largest_cross_array = largest_cross_array 
myList.largest_sublist = largest_sublist

def largest_sublist2(my_list):
    if len(my_list) == 0:
        return (None, None, None)
    largest_sum, startidx, stopidx = my_list[0], 0, 1
    survey_sum, survey_start = 0, 0
    for i, val in enumerate(my_list):
        survey_sum += val
        if survey_sum > largest_sum:
            largest_sum = survey_sum
            if survey_sum > 0:
                stopidx = i+1
                startidx = survey_start
            elif survey_sum <= 0:
                startidx = i
                stopidx = i+1
                survey_sum = 0
        else:
            if survey_sum < 0:
                survey_sum = 0
                survey_start = i+1            
    return largest_sum, startidx, stopidx

myList.largest_sublist2 = largest_sublist2