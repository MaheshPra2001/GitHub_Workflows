import unittest
from main import add

class TestMain(unittest.TestCase):
    def test_add(self):
        assert add(2,3) == 5
        assert add(-1,1) == 0


# if expected and actual outputs are same then we will get the 
# result as pass
# assert is assertion function which checking
#actual == expected
# if it matches test case passed
# run this I will use libarary pytest