#!/usr/bin/env bash

if [ $# -ne 2 ]; then
    printf "Run with two input files. For example:
    /run.sh <spec.json> <text_input.txt>\n"
    exit 1
fi

docker build -t text_fixed_file_csv .
# Run and map to current directory to enable file output
docker run -ti -v $(pwd):/app text_fixed_file_csv $1 $2