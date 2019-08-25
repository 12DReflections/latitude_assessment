#!/usr/bin/python3
import argparse
import file_reader

def main(specFile, inputFile):
    # Parse the fixed width file and to a CSV file
    file_processor = file_reader.File_Reader(specFile, inputFile)
    outcome = file_processor.run()
    if outcome is 0:
        print(outcome)
    else: print("Error code: " + outcome)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = 'To Fixed Frame, to CSV')
    parser.add_argument('inputSpec', help='Your input specification, ie: spec.json')
    parser.add_argument('inputFile', help='Your input file, ie: text_input.txt')
    args = parser.parse_args()

    specFile = args.inputSpec
    inputFile = args.inputFile

    main(specFile, inputFile)