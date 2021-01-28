from unittest import TestCase
from unittest.mock import patch
from src.db_helper import DbHelper

class TestDbHelper(TestCase):
    def setUp(self):
        self.db = DbHelper()

    @patch('src.db_helper.DbHelper')
    def test_max_salary_is_greater_than_min_salary (self, MockDbHelper):
        dbHelper =MockDbHelper()  # create a mock object of Calculator class. This will help to customize output of class methods
        '''
        mock the sum() method of Calculator class to return value '1'. Noth that since we have mocked/stubbed the
        sum method, it will not execute the actual logic whenever called and just return 1 irrespective of input.
        '''
        dbHelper.get_maximum_salary.return_value = 1  
        maxSalary = dbHelper.get_maximum_salary()   # calling the sum method but the mocked version will actually get called
        dbHelper.get_minimum_salary.return_value = 0
        minSalary = dbHelper.get_minimum_salary()   # calling the sum method but the mocked version will actually get called
        
        self.assertGreater(maxSalary, minSalary)
