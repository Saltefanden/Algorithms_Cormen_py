import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('Diller'.upper(), 'DIL2LER')



def main():
    unittest.main()

if __name__ == '__main__':
    main()


# python -m unittest -v test_module