import unittest

def setUpModule():
    print("Setup Module level")


def tearDownModule():
    print("Teardown Module level")


class fixturesUnittest(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("Setup class")

    def setUp(self):
        print("setUp Test")

    def test2(self):
        print("test 2")


    def test1(self):
        print("test 1")

    def test3(self):
        print("test 3")

    def tearDown(self):
        print("Teardown")

    @classmethod
    def tearDownClass(cls):
        print("Teardown class")
if __name__ == '__main__':
    unittest.main()
