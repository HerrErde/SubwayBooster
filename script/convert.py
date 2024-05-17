import os
import json

input_dir = "src/profile"
output_dir = "temp/data"

os.makedirs(output_dir, exist_ok=True)


def convert_json(input_file, output_file):
    try:
        with open(input_file, "r") as input_file:
            data = json.load(input_file)

        if "data" in data:
            data_content = json.dumps(data["data"]).replace(" ", "")
            new_data = {"data": data_content}

            new_data = {}
            if "version" in data:
                new_data["version"] = data["version"]

            new_data["data"] = data_content

            with open(output_file, "w") as outfile:
                json.dump(new_data, outfile, indent=2)
                print(f"File '{output_file}' created successfully.")
        else:
            print(f"Error: No 'data' field found in '{input_file}'")
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error processing '{input_file}': {e}")


for json_file in os.listdir(input_dir):
    input_file_path = os.path.join(input_dir, json_file)
    output_file_path = os.path.join(output_dir, json_file)

    convert_json(input_file_path, output_file_path)
