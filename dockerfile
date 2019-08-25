
# Text to Fixed Frame to CSV converter
FROM python:3.6
WORKDIR /app

COPY main.py file_reader.py unit_tests.py ./
COPY text_input.txt spec.json ./

# Set default value for a variable
ENTRYPOINT [ "python3", "./main.py" ]
