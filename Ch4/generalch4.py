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
from Code_to_be_tested import myList

def addone(my_list):
    returnlist = []
    for i, val in enumerate(my_list):
        returnlist.append(val +1) 
    return returnlist

myList.addone = addone 

