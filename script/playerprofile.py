import json

playerprofile_data_path = "temp/input/playerprofile_data.json"
portrait_file_path = "src/profile/profile_portrait.json"
frame_file_path = "src/profile/profile_frame.json"
background_file_path = "src/profile/profile_background.json"


def portrait():
    try:
        with open(playerprofile_data_path, "r") as data_file:
            try:
                data = json.load(data_file)  # Load data from playerprofile_data.json

                if "profilePortraits" in data:
                    # Extract portrait IDs from the profilePortraits list
                    portrait_ids = data["profilePortraits"]

                    # Create a dictionary to store portrait data with the specified structure
                    portrait_data = {
                        "version": 1,
                        "data": {"selected": "jake_portrait", "owned": {}},
                    }

                    # Populate portrait_data["data"]["portraits"] with each portrait ID and default isSeen value
                    for portrait_id in portrait_ids:
                        portrait_data["data"]["owned"][portrait_id] = {
                            "id": portrait_id,
                            "isSeen": True,
                        }

                    # Save portrait_data to profile_portrait.json
                    with open(portrait_file_path, "w") as file:
                        json.dump(portrait_data, file, indent=2)

                else:
                    print("Error: 'profilePortraits' key not found")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {playerprofile_data_path}: {e}")

    except IOError as e:
        print(f"Error opening or accessing {playerprofile_data_path}: {e}")


def frame():
    try:
        with open(playerprofile_data_path, "r") as data_file:
            try:
                data = json.load(data_file)  # Load data from playerprofile_data.json

                if "profileFrames" in data:
                    # Extract frame IDs from the profileFrames list
                    frame_ids = data["profileFrames"]

                    # Create a dictionary to store frame data with the specified structure
                    frame_data = {
                        "version": 1,
                        "data": {"selected": "default_frame", "owned": {}},
                    }

                    # Populate frame_data["data"]["owned"] with each frame ID and default isSeen value
                    for frame_id in frame_ids:
                        frame_data["data"]["owned"][frame_id] = {
                            "id": frame_id,
                            "isSeen": True,
                        }

                    # Save frame_data to frame_file_path
                    with open(frame_file_path, "w") as file:
                        json.dump(frame_data, file, indent=2)

                else:
                    print("Error: 'profileFrames' key not found in the data")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {playerprofile_data_path}: {e}")

    except IOError as e:
        print(f"Error opening or accessing {playerprofile_data_path}: {e}")


def background():
    try:
        with open(playerprofile_data_path, "r") as data_file:
            try:
                data = json.load(data_file)  # Load data from playerprofile_data.json

                if "profileBackgrounds" in data:
                    # Extract portrait IDs from the profilePortraits list
                    background_ids = data["profileBackgrounds"]

                    # Create a dictionary to store background data with the specified structure
                    background_data = {
                        "version": 1,
                        "data": {"selected": "default_frame", "owned": {}},
                    }

                    # Populate portrait_data["data"]["portraits"] with each portrait ID and default isSeen value
                    for background_id in background_ids:
                        background_data["data"]["owned"][background_id] = {
                            "id": background_id,
                            "isSeen": True,
                        }

                    # Save portrait_data to profile_portrait.json
                    with open(background_file_path, "w") as file:
                        json.dump(background_data, file, indent=2)

                else:
                    print("Error: 'profilePortraits' key not found")

            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in {playerprofile_data_path}: {e}")

    except IOError as e:
        print(f"Error opening or accessing {playerprofile_data_path}: {e}")


portrait()
frame()
background()
