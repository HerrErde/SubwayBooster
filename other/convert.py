import json
import sys


def convert(input_file_name):
    output_file_name = input_file_name.replace(".json", "-gen.json")

    try:
        with open(input_file_name, "r") as input_file:
            data = json.load(input_file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error processing '{input_file_name}': {e}")
        return

    new_data = {
        "version": data.get("version", ""),
        "data": json.dumps(data.get("data", "")).replace(" ", ""),
    }

    with open(output_file_name, "w") as output_file:
        json.dump(new_data, output_file, indent=2)

    print(f"File '{output_file_name}' created successfully.")


if len(sys.argv) == 2:
    convert(sys.argv[1])
