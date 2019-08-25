# Data Engineering Coding Challenges

## Runtime Instructions
``` bash
# Run in docker 
./run.sh spec.json text_input.txt
# Run in Python
python3 main.py spec.json text_input.txt
```
The output csv is generated to [csv_output.csv](csv_output.csv).
The fixed frame file is generated to [fixed_frame.lat](fixed_frame.lat).

## Judgment Criteria
- Beauty of the code (beauty lies in the eyes of the beholder)
- Testing strategies
- Basic Engineering principles

## Parse fixed width file
- Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
- Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
- DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
- Language choices (Python or Scala)
- Deliver source via github or bitbucket
- Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
- Pay attention to encoding

# Docker Build and Run in Current Directory
* Note to output the csv outside the docker container we map the container to the current working directory. To build and run use the `run.sh` script as above, to run separately from the build, the commands are as below,
``` bash
docker build -t text_fixed_file_csv .
docker run -ti -v $(pwd):/app text_fixed_file_csv spec.json text_input.txt
```