#!/usr/bin/python3

from file_reader import File_Reader

def main():
    # Parse the fixed width file and to a CSV file
    file_processor = File_Reader()
    outcome = file_processor.run()
    if outcome is 0:
        print(outcome)
    else: print("Error code: " + outcome)

if __name__ == "__main__":
    main()