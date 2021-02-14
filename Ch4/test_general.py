import pytest
from generalch4 import myList

def test_add_one():
    print('lol')
    assert myList([1,2,3]).addone() == [2,3,4]

#Ikke den pæneste opsætning, se om du kan lave det som et dictionary udenfor med test + ids 
@pytest.mark.parametrize("test_input, expected",[([-1,-1,1,1,1,-1-1], (3,2,5)), #0Regular test
                                                ([13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7], (43,7,11)),  #1As per the book with updated indexing
                                                ([-1, -1], (-1,0,1)), #2What to return in this case?
                                                ([-2,-1], (-1,1,2)), #3Ensure that not just the left sum gets returned
                                                ([], (None,None,None)), #4Handle empty lists
                                                ([14,14,14,14], (14*4, 0, 4)), #5Handle entire list
                                                ([-300,-300,100,-300,-300], (100,2,3)), #6Handle middle only
                                                ([140,0,-100,100,40,0, 0],(180,0,5) ), #7Another regular john
                                                ([10, 0, 0, 0, 0, 0], (10,0,1)), #8 Are extra zeros added?
                                                ([1,2,1,-4,4], (4, 0,3)), #9Right preference? Right over middle at least
                                                ([1,2,1,0,0,0,-4,4], (4, 0,3)), #10Right preference? Right over middle at least
                                                ([0,-1,2,-3,4,-5],(4,4,5)),#lort
                                                ])  
@pytest.mark.parametrize("Function", ["myList(test_input).largest_sublist()", "myList(test_input).largest_sublist2()"], ids=['slow', 'fast'])
def test_largest_sub_array(test_input, expected, Function):
    assert eval(Function) == expected