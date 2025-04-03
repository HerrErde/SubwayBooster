import json

with open("temp/input/calendar_data.json", "r", encoding="utf-8") as f:
    calendar_data = json.load(f)
    calendar_id = calendar_data.get("calendarId")

new_data = {
    "version": 3,
    "data": {
        "lastSaved": "1970-01-01T00:00:00Z",
        "calendarStates": {},
        "completedCalendars": {calendar_id: True},
    },
}


with open("src/profile/calendars.json", "w") as calendar_file:
    json.dump(new_data, calendar_file, indent=2)
