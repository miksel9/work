#!/usr/bin/Python

from chrome import advertiser

import unittest

class testSignup(unittest.TestCase):

    def testAdvertiserSignup(self):
        advertiser.signup()


if __name__ == "__main__":
    unittest.main()