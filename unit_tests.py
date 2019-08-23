#!/usr/bin/python3
import unittest
from file_reader import File_Reader

class TestString(unittest.TestCase):

    def setUp(self):
        self.file_processor = File_Reader()

    ''' Generate the windows-1252 file and validate edge cases'''
    # Generate a fixed width file from the spec file
    def test_generate_fixed_width_fix(self):
        pass

    def test_boundaries_of_fixed_width(self):
        pass

    ''' Parse windows-1252 to CSV file '''
    def test_parse_fixedwidth_to_csv(self):
        pass
    
    def test_parse_wrong_file_type(self):        
        pass

    def test_parse_no_files(self):        
        pass

    ''' Test Reading config file '''
    def config_file_input(self):
        pass

    def test_column_names(self):
        pass

    def offsets_exist(self):
        pass

    def encodings_exist(self):
        pass

if __name__ == "__main__":
    unittest.main()