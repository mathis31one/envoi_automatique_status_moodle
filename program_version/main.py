import json
from envoi_status import evoyer_status


with open("program_version\\settings.json", "r") as settings_file:
    settings = json.load(settings_file)
    for profile in settings["profiles"]:
        evoyer_status(settings["chrome_location"],settings["user_profile_dir"],profile)