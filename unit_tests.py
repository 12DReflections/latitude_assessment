#!/usr/bin/python3
import unittest
from file_reader import File_Reader

class TestString(unittest.TestCase):

    # def setUp(self):
    #     file_processor = File_Reader()

    ''' Test Reading config file '''
    def config_file_input(self):
        pass

    def test_column_count_is_offset_count(self):
        f = File_Reader()
        spec_data = f.input_spec(f.spec_filepath)
        self.assertEqual(len(spec_data["ColumnNames"]), len(spec_data["Offsets"]))

    def test_spec_file_input_success(self):
        f = File_Reader()
        spec_data = f.input_spec(f.spec_filepath)
        self.assertTrue(type(spec_data) is dict)

    def test_create_offset(self):
        pass

    # def test_offset_frame_length(self):
    #     file_processor = File_Reader()
    #     column_names, offsets, include_header, input_encoding, output_encoding = file_processor.input_spec(file_processor.input_file, file_processor.spec_filepath)
    #     self.assertEqual(len(column_names), len(offsets))

    def offsets_exist(self):
        pass

    def encodings_exist(self):
        pass


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

if __name__ == "__main__":
    unittest.main()