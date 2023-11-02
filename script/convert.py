import os
import json

input_dir = "src/profile"
output_dir = "temp"

os.makedirs(output_dir, exist_ok=True)

# Get a list of all JSON files in the input folder
json_files = [f for f in os.listdir(input_dir)]


def convert_json(input_file, output_file):
    with open(input_file, "r") as input_file:
        data = json.load(input_file)

    # Remove spaces from the "data" field
    data_content = json.dumps(data["data"]).replace(" ", "")

    # Create a new JSON object with the modified "data" field
    new_data = {"version": data["version"], "data": data_content}

    # Save the new JSON object to the output file
    with open(output_file, "w") as output:
        json.dump(new_data, output, indent=2)
        print(f"File '{output_file}' created successfully.")


for json_file in json_files:
    input_file_path = os.path.join(input_dir, json_file)
    output_file_path = os.path.join(output_dir, json_file)

    convert_json(input_file_path, output_file_path)
