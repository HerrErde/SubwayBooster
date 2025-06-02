import json

input_data_path = "temp/input/cities_data.json"
output_file_path = "src/profile/user_stats.json"

try:
    with open(output_file_path, "r+") as file:
        try:
            data = json.load(file)

            world_visited = data["data"].get("worldDestinationVisited", {})

            with open(input_data_path, "r", encoding="utf-8") as input_data_file:
                cities_data = json.load(input_data_file)
                entry_names = cities_data.get("cities", [])

            for entry_name in entry_names:
                world_visited[entry_name] = 1

            with open(output_file_path, "w") as output_file:
                json.dump(data, output_file, indent=2)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error decoding JSON or key error in user_stats.json: {e}")

except IOError as e:
    print(f"Error opening or accessing user_stats.json: {e}")
