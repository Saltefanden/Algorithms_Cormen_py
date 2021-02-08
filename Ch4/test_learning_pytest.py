import Code_to_be_tested as extmod

def test_sort():
    assert extmod.myList([3,2,1]).insertion_sort() == [1,2,3]
    assert extmod.myList([1]).insertion_sort() == [1]
    assert extmod.myList([]).insertion_sort() == []


# Fortsæt her: https://docs.pytest.org/en/stable/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

# as testing two lists for equality is at the worst case Th(n) use 
# assert all(array[i-1] <= array[i] for i in range(1,length(array))) 
# rather than providing a pre sorted list for checks