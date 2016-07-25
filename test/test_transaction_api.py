# coding: utf-8

"""
Copyright 2016 SmartBear Software

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

   ref: https://github.com/swagger-api/swagger-codegen
"""

from __future__ import absolute_import

import os
import sys
import unittest

import squareconnect
from squareconnect.rest import ApiException
from squareconnect.apis.transaction_api import TransactionApi


class TestTransactionApi(unittest.TestCase):
    """ TransactionApi unit test stubs """

    def setUp(self):
        self.api = squareconnect.apis.transaction_api.TransactionApi()

    def tearDown(self):
        pass

    def test_capture_transaction(self):
        """
        Test case for capture_transaction

        CaptureTransaction
        """
        pass

    def test_charge(self):
        """
        Test case for charge

        Charge
        """
        pass

    def test_list_transactions(self):
        """
        Test case for list_transactions

        ListTransactions
        """
        pass

    def test_retrieve_transaction(self):
        """
        Test case for retrieve_transaction

        RetrieveTransaction
        """
        pass

    def test_void_transaction(self):
        """
        Test case for void_transaction

        VoidTransaction
        """
        pass


if __name__ == '__main__':
    unittest.main()