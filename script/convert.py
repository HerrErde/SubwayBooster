import os
import json


def process_json_file(input_file_name, output_file_name):
    try:
        # Read the input JSON file
        with open(input_file_name, "r") as input_file:
            data = json.load(input_file)

        # Extract the content of the "data" field
        data_content = json.dumps(data["data"], separators=(",", ":"))

        # Create a new JSON object with the modified "data" field
        new_data = {"version": data["version"], "data": data_content}

        # Save the new JSON object to the output file
        with open(output_file_name, "w") as output_file:
            json.dump(new_data, output_file, indent=2)

        print(f"File '{output_file_name}' created successfully.")
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error processing '{input_file_name}': {str(e)}")


def main():
    # Input folder containing JSON files
    input_folder = "src/profile"

    # Output folder for the modified JSON files
    output_folder = "temp"

    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all JSON files in the input folder
    json_files = [f for f in os.listdir(input_folder) if f.endswith(".json")]

    # Process each JSON file in the input folder
    for json_file in json_files:
        # Construct the full path for input and output files
        input_file_path = os.path.join(input_folder, json_file)
        output_file_path = os.path.join(output_folder, json_file)

        # Process the JSON file
        process_json_file(input_file_path, output_file_path)
