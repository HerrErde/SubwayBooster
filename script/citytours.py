import json

input_file_path = "temp/input/citytours_data.json"
output_file_path = "src/profile/city_tours.json"

try:
    with open(input_file_path, "r", encoding="utf-8") as data_file:
        data = json.load(data_file)

    city_tours = []

    for tourId in data:
        if tourId:
            city_tours.append(tourId)

    final_data = {
        "lastSaved": "1970-01-01T00:00:00Z",
        "cityTourInstances": {},
        "completedCityTours": city_tours,
    }

    output_data = {"version": 1, "data": final_data}

    with open(output_file_path, "w", encoding="utf-8") as f:
        json.dump(output_data, f, indent=2)

except IOError as e:
    print(f"Error opening or accessing {input_file_path}: {e}")

except json.JSONDecodeError as e:
    print(f"Error decoding JSON from {input_file_path}: {e}")
