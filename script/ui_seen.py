import json

mailbox_data_path = "temp/input/mailbox_data.json"
promotions_data_path = "temp/input/promotions_data.json"
collections_file = "temp/input/collections_data.json"
output_file_path = "src/profile/ui_seen.json"


with open(collections_file, "r", encoding="utf-8") as file:
    data = json.load(file)
    time_slot = data.get("timeSlot", "")

try:
    with open(output_file_path, "r+", encoding="utf-8") as file:
        try:
            data = json.load(file)

            with open(promotions_data_path, "r", encoding="utf-8") as promotions_file:
                promotions_data = json.load(promotions_file)

                promotions_seen_info = {}

                for promotion in promotions_data:
                    promotion_id = promotion.get("id", "")
                    if promotion_id:
                        promotions_seen_info[promotion_id] = {
                            "lastSeenTime": "1970-01-01T00:00:00Z",
                            "removeAtTime": "9999-12-31T00:00:00Z",
                            "opened": True,
                        }

                data["data"]["promotionsSeenInfo"] = promotions_seen_info

            with open(mailbox_data_path, "r", encoding="utf-8") as mailbox_data_file:
                mailbox_data = json.load(mailbox_data_file)
                entry_names = mailbox_data.get("entries", [])

                local_mails_seen = {
                    entry_name: "1970-01-01T00:00:00Z" for entry_name in entry_names
                }

                data["data"]["newSeasonPopupShownForID"] = time_slot
                data["data"]["localMailsSeenEntries"] = local_mails_seen

            popup_seen_info = {"popupSeenInfo": {}}
            for key in range(3, 53):
                popup_seen_info["popupSeenInfo"][str(key)] = {
                    "lastSeenTime": "9999-12-31T00:00:00Z",
                    "totalTimesSeen": 1,
                    "dailyTimesSeen": 1,
                }

            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error decoding JSON or key error in ui_seen.json: {e}")

except IOError as e:
    print(f"Error opening or accessing ui_seen.json: {e}")
