#!/usr/bin/python3

import file_reader

def main():
    # Parse the fixed width file and to a CSV file
    file_processor = file_reader.File_Reader()
    outcome = file_processor.run()
    if outcome is 0:
        print(outcome)
    else: print("Error code: " + outcome)

if __name__ == "__main__":
    main()