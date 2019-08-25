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
        # Currently outputs to fixed_framed.lat
        fixed_frame = self.convert_to_fixed_width(spec_data, self.input_file)
        print("Fixed frame file save location: " + fixed_frame)
        csv_output = self.parser(spec_data, fixed_frame)
        print("CSV Output save location: " + csv_output)
        return 0

    def input_spec(self, specfile):
        try:
            with open(specfile) as json_file:
                spec_data = json.load(json_file)
        except Exception as err:
            logging.error('Cannot load the spec')
            logging.error(err)

        # Convert to variables from unicode in the spec
        offset_integers = []
        for sub in spec_data['Offsets']:
            offset_integers.append(int(sub))
        spec_data['Offsets'] = offset_integers
        spec_data['IncludeHeader'] = bool(spec_data['IncludeHeader'])
        
        return spec_data

    # A parser that can parse the fixed width file and generate a CSV
    def parser(self, spec, fixed_frame_input_file="fixed_frame.lat"):
        try:
            f = io.open(fixed_frame_input_file, mode="r", encoding="cp1252")
            fixed_frame = f.readlines()
            output_csv = 'csv_output.csv'

            # Strip whitespace and write to CSV
            with open(output_csv,'w') as file:
                for line in fixed_frame:
                    cleaned_string = ','.join([w.strip() for w in line.split(';')])
                    file.write(cleaned_string + '\n')
            f.close()
        except Exception as err:
            logging.error(err)
        return output_csv

    def convert_to_fixed_width(self, spec_data, input_file):
        # Generate fixed line file with delimeters showing frames
        frame_offsets = self.get_frame_offsets(spec_data)
        output_file = 'fixed_frame.lat'
        with open(input_file, 'r') as f:
            with codecs.open(output_file, 'wb', 'cp1252') as writer:
                if spec_data['IncludeHeader']:
                    column_headers = ''
                    for h in spec_data['ColumnNames']:
                        column_headers += h + ';'
                    column_headers = self.header_splitter(spec_data['ColumnNames'], spec_data['Offsets'])
                    writer.write(column_headers)
                # Apply the fixed line delimeters and write to encoded file
                for line_index, line in enumerate(f.readlines()):
                    splitted_line = self.line_splitter(line, frame_offsets)
                    writer.write(splitted_line)
        return output_file

    def header_splitter(self, line, frame_offsets, delimiter = ';'):
        # Split a line at the frame offsets
        line_fixed = ''
        for i, n in enumerate(frame_offsets):
            # Build the line [TODO] switch to inline string one-liner
            fixed_frames = ' ' * (int(frame_offsets[i]) - 2)
            line_fixed += line[i]
            line_fixed +=  fixed_frames + delimiter
        return line_fixed

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