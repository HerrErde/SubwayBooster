import os
import json

input_dir = "src/profile"
output_dir = "temp/data"

os.makedirs(output_dir, exist_ok=True)


def convert_json(input_file_path, output_file_path):
    try:
        with open(input_file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if "data" in data:
            # Minify the "data" field
            data_content = json.dumps(data["data"], separators=(",", ":"))
            new_data = {"data": data_content}

            if "version" in data:
                new_data["version"] = data["version"]

            with open(output_file_path, "w", encoding="utf-8") as f:
                json.dump(new_data, f, separators=(",", ":"))

            print(f"File '{output_file_path}' created successfully.")
        else:
            print(f"Error: No 'data' field found in '{input_file_path}'")

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error processing '{input_file_path}': {e}")


for json_file in os.listdir(input_dir):
    if json_file.endswith(".json"):
        input_file_path = os.path.join(input_dir, json_file)
        output_file_path = os.path.join(output_dir, json_file)
        convert_json(input_file_path, output_file_path)
