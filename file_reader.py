import io
import json

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
        print(spec_data)
        return 0

    def input_spec(self, specfile):

        with open(specfile) as json_file:
            spec_data = json.load(json_file)
        # Debug sample return
        # return ['f1'], [2], True, "windows-1252", "utf-8"  
        return spec_data


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
        
