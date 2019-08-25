#!/usr/bin/env bash

docker build -t text_fixed_file_csv .
docker run -ti -v $(pwd):/app text_fixed_file_csv