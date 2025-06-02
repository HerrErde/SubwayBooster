import json

playerprofile_data_path = "temp/input/playerprofile_data.json"
portrait_file_path = "src/profile/profile_portrait.json"
frame_file_path = "src/profile/profile_frame.json"
background_file_path = "src/profile/profile_background.json"


def portrait():
    try:
        with open(playerprofile_data_path, "r", encoding="utf-8") as data_file:
            try:
                data = json.load(data_file)

                if "profilePortraits" in data:
                    portrait_ids = data["profilePortraits"]

                    portrait_data = {
                        "version": 1,
                        "data": {"selected": "jake_portrait", "owned": {}},
                    }

                    for portrait_id in portrait_ids:
                        portrait_data["data"]["owned"][portrait_id] = {
                            "id": portrait_id,
                            "isSeen": True,
                        }

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
        with open(playerprofile_data_path, "r", encoding="utf-8") as data_file:
            try:
                data = json.load(data_file)

                if "profileFrames" in data:
                    frame_ids = data["profileFrames"]

                    frame_data = {
                        "version": 1,
                        "data": {"selected": "default_frame", "owned": {}},
                    }

                    for frame_id in frame_ids:
                        frame_data["data"]["owned"][frame_id] = {
                            "id": frame_id,
                            "isSeen": True,
                        }

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
        with open(playerprofile_data_path, "r", encoding="utf-8") as data_file:
            try:
                data = json.load(data_file)

                if "profileBackgrounds" in data:
                    background_ids = data["profileBackgrounds"]

                    background_data = {
                        "version": 1,
                        "data": {"selected": "default_frame", "owned": {}},
                    }

                    for background_id in background_ids:
                        background_data["data"]["owned"][background_id] = {
                            "id": background_id,
                            "isSeen": True,
                        }

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
