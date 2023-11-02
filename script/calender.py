import json

with open("calendar_data.json", "r") as calendar_data_file:
    calendar_data = json.load(calendar_data_file)
    calendar_id = calendar_data.get("id")

new_data = {
    "version": 3,
    "data": {
        "lastSaved": None,
        "calendarStates": {},
        "completedCalendars": {calendar_id: True},
    },
}


with open("src/profile/calendars.json", "w") as calendar_file:
    json.dump(new_data, calendar_file, indent=2)
