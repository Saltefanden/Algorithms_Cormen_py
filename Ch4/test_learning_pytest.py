import Code_to_be_tested as extmod

def test_sort():
    assert extmod.myList([3,2,1]).insertion_sort() == [1,2,3]