import unittest
#exernally
def sum(x,y):
    return x+y;

def sub(a,b):
    return a-b

class SampleTest(unittest.TestCase):

    @unittest.expectedFailure
    def test_calc(self):
      print(sum(4,5))

    def test1(self):
        self.assertEqual(sum(4,5),9)


    def test2(self):
        self.assertEqual(sum(4,5),8)
if __name__ == '__main__':
    unittest.main()