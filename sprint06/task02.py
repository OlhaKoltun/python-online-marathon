# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name")
#by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it). 
# Use pretty printing for writing users to json-file.

import json
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

def parse_user(output_file, *input_files):
    source = []
    unique_name = set()
    for file in input_files:
        try:
            with open(file, 'r') as in_f:
                data = json.load(in_f)
                for item in data:
                    if 'name' in item.keys() and item['name'] not in unique_name:
                        source.append(item)
                        unique_name.add(item['name'])
        except FileNotFoundError as e:
            logging.error(f'File {e.filename} doesn\'t exist')

    with open(output_file, 'w') as out_f:
        json.dump(source, out_f, indent=4)
