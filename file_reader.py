import io
import json
import logging
import codecs
import re

class File_Reader:
    '''Create the file reader class'''
    '''The class reads in a spec file and an input file. 
       First the input file is converted into windows-1252 encoding,
       then the file is decoded to a CSV file.'''

    def __init__(self, spec_name='spec.json', input_file='text_input.txt'):
        self.spec_filepath = spec_name
        self.input_file = input_file

    def run(self):
        f = File_Reader()
        spec_data = self.input_spec(f.spec_filepath)
        convert_result = self.convert_to_fixed_width(spec_data, self.input_file)
        print(convert_result)
        return 0

    def input_spec(self, specfile):
        try:
            with open(specfile) as json_file:
                spec_data = json.load(json_file)
        except Exception as err:
            logging.error('Cannot load the spec')
            logging.error(err)

        # Convert spec integers and booleans from unicode
        offset_integers = []
        for sub in spec_data['Offsets']:
            offset_integers.append(int(sub))
        spec_data['Offsets'] = offset_integers
        spec_data['IncludeHeader'] = bool(spec_data['IncludeHeader'])
        
        return spec_data

    def convert_to_fixed_width(self, spec_data, input_file):
        # Generate fixed line file with delimeters showing frames
        frame_offsets = self.get_frame_offsets(spec_data)

        with open(input_file, 'r') as f:
            with codecs.open('fixed_frame.lat', 'wb', 'cp1252') as writer:
                if spec_data['IncludeHeader']:
                    column_headers = ''
                    for h in spec_data['ColumnNames']:
                        column_headers += h + ';'
                    column_headers +='\n'
                # Apply the fixed line delimeters and write to encoded file
                for line_index, line in enumerate(f.readlines()):
                    if line_index == 1 or len(line) == 0:
                        continue
                    splitted_line = self.line_splitter(line, frame_offsets)
                    writer.write(splitted_line)
        return 0

    def line_splitter(self, line, frame_offsets, delimiter = ';'):
        # Split a line at the frame offsets
        for i, n in enumerate(frame_offsets):
            if i == len(frame_offsets) - 1:
                continue
            line = re.sub(r"^(.{%d})()" % (n + i), r"\1%s" % delimiter, line)
        return line

    def get_frame_offsets(self, spec_data):
        # Get the aggregate offsets to return the spacing
        aggregate_offset = []
        for i, width in enumerate(spec_data['Offsets']):
            if i == 0:
                aggregate_offset.append(int(width))
            else:
                distance_sum = width + aggregate_offset[i-1]
                aggregate_offset.append(distance_sum)
        return aggregate_offset
        

    # [TODO] Generate a fixed width file from the spec file
    # [Bonus] Creates a windows formatted file 
    def file_generator_fixed_width(self, filepath, ):
        ''' Spike fixed width [TODO] enable lines to wrap'''
        # widths=(4,10,10)
        # items=(1,"ONE",2)
        # k = "".join("%*s" % i for i in zip(widths, items))
        # print(k)
        # with open(filepath, "w") as text_file:
        #     text_file.write("%s" % (k))
        # pass
    
    # A parser that can parse the fixed width file and generate a CSV
    def parser(self, input_file, spec):        
        pass
        
