import json
from envoi_status import evoyer_status

with open("program_version\\accounts.json", "r") as accounts_file:
    accounts = json.load(accounts_file)
    for key in accounts:
        evoyer_status(key,accounts[key])