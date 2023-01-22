import time
import unittest
import timeout_decorator

class testtimeout(unittest.TestCase):

    @timeout_decorator.timeout(5)
    def testtimeout(self):
        time.sleep(10)
        print("hello")


if __name__ == '__main__':
    unittest.main()