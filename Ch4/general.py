print('__file__={0:<35} | __name__={1:<20} | __package__={2:<20}'.format(__file__,__name__,str(__package__)))
from Ch2 import general as g 
print(g.myList([2,3,5,1,3,6,23,0,-12,1,4,2,5]).merge_sort())
print("We did it boissss")