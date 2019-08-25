#!/usr/bin/python3
import unittest
from file_reader import File_Reader

class TestString(unittest.TestCase):

    # def setUp(self):
    #     file_processor = File_Reader()

    ''' Test Reading config file '''
    @classmethod
    def setUpClass(self):
        self.f = File_Reader()

    def test_column_count_is_offset_count(self):        
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertEqual(len(spec_data["ColumnNames"]), len(spec_data["Offsets"]))

    def test_line_splitter_type(self):
        # Test line splitter returns a string successfully
        line = "don't worry about a thing"

        spec_data = self.f.input_spec(self.f.spec_filepath)
        frame_offsets = self.f.get_frame_offsets(spec_data)

        res = self.f.line_splitter(line, frame_offsets)
        self.assertTrue(type(res) is str)

    def test_output_csv(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        # frame_offsets = self.f.get_frame_offsets(spec_data)
        fixed_frame = self.f.convert_to_fixed_width(spec_data, self.f.input_file)
        csv_output = self.f.parser(spec_data, fixed_frame)
        self.assertEqual(csv_output, "csv_output.csv")

    def test_spec_file_input_success(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertTrue(type(spec_data) is dict)

    def test_delimiting_coding_exist(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertTrue(spec_data['DelimitedEncoding'])

    def test_offsets_exist(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertTrue(spec_data['Offsets'])
        
    def test_encodings_exist(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertTrue(spec_data['FixedWidthEncoding'])

    def test_include_header_exist(self):
        spec_data = self.f.input_spec(self.f.spec_filepath)
        self.assertTrue(spec_data['IncludeHeader'])


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