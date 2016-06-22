#!/usr/bin/Python

import advertiserSignup
import publisherSignup

import unittest

class testSignup(unittest.TestCase):

    def testPublisherSignup(self):
        publisherSignup.signup()

    def testAdvertiserSignup(self):
        advertiserSignup.signup()


if __name__ == "__main__":
    unittest.main()