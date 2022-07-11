from copyreg import constructor
from typing_extensions import Self
import unittest
import os.path


class TestStringMethods(unittest.TestCase):
    
    
    def test_isFileExist(self):
        
        print("enter the input file name")
        filePath = input()
        
        fileExistCheck = os.path.exists(filePath)
        self.assertTrue(fileExistCheck)        

    def test_isfileEmpty(self):
        
        print("enter the input file name")
        filePath = input()
        
        isFileEmpty = os.stat(filePath).st_size == 0
        self.assertFalse(isFileEmpty)

  
# unittest.main()

TestStringMethods()
