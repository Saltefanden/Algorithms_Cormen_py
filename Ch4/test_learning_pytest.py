import Code_to_be_tested as extmod
import pytest

# %% Had tons of boilerplate for each sortmethod
# def test_sort():
#     assert extmod.myList([3,2,1]).insertion_sort() == [1,2,3]
#     assert extmod.myList([1]).insertion_sort() == [1]
#     assert extmod.myList([]).insertion_sort() == []


# %% Reduce some of the boilerplate by using a simple fixture
@pytest.fixture
def input_list():
    return [1,2,3,2,1,0,1]

@pytest.fixture
def expected_list():
    return [0,1,1,1,2,2,3]


def test_insertionsort(input_list,expected_list):
    assert extmod.myList(input_list).insertion_sort() == expected_list

def test_mergesort(input_list,expected_list):
    assert extmod.myList(input_list).merge_sort() == expected_list


# %% Reduce more by adding parametrized tests

ids = ["Empty", "Single element", "Multi-same element", "Pre-sorted",
        "Unsorted"]
@pytest.fixture(params=[[], [0], [1,1], [1,2,3], [1,2,3,2,1,0,1]], ids=ids)
def inp_list(request):
    return request.param 

@pytest.fixture
def exp_list(inp_list):
    return sorted(inp_list)

def test_inssort(inp_list, exp_list):
    assert extmod.myList(inp_list).insertion_sort() == exp_list

def test_mergesrt(inp_list, exp_list):
    assert extmod.myList(inp_list).merge_sort() == exp_list


# Fortsæt her: https://docs.pytest.org/en/stable/fixture.html#scope-sharing-fixtures-across-classes-modules-packages-or-session

# as testing two lists for equality is at the worst case Th(n) use 
# assert all(array[i-1] <= array[i] for i in range(1,length(array))) 
# rather than providing a pre sorted list for checks --- Something about the elements also being present 
# Alternatively just do the sorted first check simple, then add the elements present,
# then add full equality of lists.


# %% Used for examples in online material.
class Fruit:
    def __init__(self, name):
        self.name = name

    # def __eq__(self, other): # Ensures that equality tests are based on name only and not memory address
    #     return self.name == other.name


@pytest.fixture
def my_fruit():
    return Fruit("apple")


@pytest.fixture
def fruit_basket(my_fruit):
    return [Fruit("banana"), my_fruit]


# Passing fixtures as arguments to testfunctions finds the fixtures, runs them, and inserts any
# return values as the argument to the function. - Thus here we have my_fruit taking the place
# of the fixtures returnvalue: Fruit('apple'). In the fruit_basket fixture we already call the
# my_fruit fixture, where once again the return value of Fruit('apple') is inserted. Thus fruit
# basket in total returns the list [Fruit("banana"), Fruit("apple")] and this is taking the place
# of the fruit_basket fixture name in the test function. We thus check if Fruit("apple") is in
# [Fruit("banana"), Fruit("apple")]. The equality operator of the Fruit class is overloaded such
# that only equality of names are enough to return true. (Somethingsomething about the objects 
# themselves might be different instances of the class? Might not, depending on how the fixture
# is called) The fixtures are called each time they are used, so the objects would in fact be
# different instances of the Fruit class - Disproved by removing the overriding of __eq__. This
# would only be the case if different tests had been calling the same fixture. 
# The documentation mentions that as well: 
# https://docs.pytest.org/en/stable/fixture.html#fixtures-can-be-requested-more-than-once-per-test-return-values-are-cached|

def test_my_fruit_in_basket(my_fruit, fruit_basket):
    assert my_fruit in fruit_basket
    assert my_fruit == fruit_basket[1]


# class Fruit:
#     def __init__(self, name):
#         self.name = name
#         self.cubed = False

#     def cube(self):
#         self.cubed = True


# class FruitSalad:
#     def __init__(self, *fruit_bowl):
#         self.fruit = fruit_bowl
#         self._cube_fruit()

#     def _cube_fruit(self):
#         for fruit in self.fruit:
#             fruit.cube()



"""Last idea is to add the unittest to both implementation algorithms following this example https://stackoverflow.com/questions/29939842/how-to-reuse-the-same-tests-to-test-different-implementations
Use parameterized tests with your tested functions as a parameter.

For example, using ddt module for parameterized testing:

def sum1(list1):
    return sum(list1)

def sum2(list1):
    res = 0
    for x in list1:
        res += x
    return res

import unittest
from ddt import ddt, data

@ddt
class SumTest(unittest.TestCase):

    @data(sum1, sum2)
    def test_sum(self, param):
        self.assertEqual(param([1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()
In this example, you have two functions "sum1" and "sum2" implementing the same algorithm: summing of list elements. In your test class, you have only one testing method "test_sum" that takes the concrete summing function as a parameter. The two summing functions are specified as a list of values for a parameterized test.

You can install "ddt" with pip:

__________________________________________

Remember you can have multiple parameters in your fixtures, and they will run all combinations of both
SEE last line above this paragraph https://docs.pytest.org/en/stable/parametrize.html#basic-pytest-generate-tests-example



"""