import json

mailbox_data_path = "temp/input/mailbox_data.json"
output_file_path = "src/profile/ui_seen.json"

try:
    with open(output_file_path, "r+") as file:
        try:
            # Load existing data from ui_seen.json
            data = json.load(file)

            # Read entry names from mailbox_data.json
            with open(mailbox_data_path, "r") as mailbox_data_file:
                mailbox_data = json.load(mailbox_data_file)
                entry_names = mailbox_data.get("entries", [])

            # Replace the existing "localMailsSeen" dictionary with new entries
            local_mails_seen = {entry_name: True for entry_name in entry_names}

            # Update the data with the new "localMailsSeen" dictionary
            data["data"]["localMailsSeen"] = local_mails_seen

            # Write the updated data back to ui_seen.json
            file.seek(0)
            json.dump(data, file, indent=2)
            file.truncate()

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error decoding JSON or key error in ui_seen.json: {e}")

except IOError as e:
    print(f"Error opening or accessing ui_seen.json: {e}")
