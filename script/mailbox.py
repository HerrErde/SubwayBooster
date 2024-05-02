import json

mailbox_data_path = "temp/input/mailbox_data.json"
output_file_path = "src/profile/ui_seen.json"

try:
    with open(output_file_path, "r+") as file:
        try:
            # Load existing data from ui_seen.json
            data = json.load(file)

            # Get the existing "localMailsSeen" dictionary from the data
            local_mails_seen = data["data"].get("localMailsSeen", {})

            # Read entry names from mailbox_data.json
            with open(mailbox_data_path, "r") as mailbox_data_file:
                mailbox_data = json.load(mailbox_data_file)
                entry_names = mailbox_data.get("entries", [])

            # Update the existing "localMailsSeen" dictionary with new entries
            for entry_name in entry_names:
                local_mails_seen[entry_name] = True

            # Write the updated data back to ui_seen.json
            with open(output_file_path, "w") as output_file:
                json.dump(data, output_file, indent=2)

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error decoding JSON or key error in ui_seen.json: {e}")

except IOError as e:
    print(f"Error opening or accessing ui_seen.json: {e}")
