from utils.db import db
from utils.data_parser import parser
import os
from os.path import dirname, join
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '/utils/.env')
load_dotenv(dotenv_path)

data_path = os.getenv('DATA_PATH')
DATA_FOLDER = os.listdir(data_path)

for folder in DATA_FOLDER:
    DATA = {
        "folder_id": parser.get_folder_id(folder),
        "region": parser.get_folder_region(folder)
    }
    local_path = join(data_path, folder)
    for path in os.listdir(local_path):
        file = os.path.join(local_path, path)
        if os.path.isfile(file):
            res = {}
            if path.split(".txt")[0] == "ImportantAutofills":
                res = parser.handle_ImportantAutofills(file)

            if path.split(".txt")[0] == "DomainDetects":
                res = parser.handle_DomainDetects(file)

            if path.split(".txt")[0] == "InstalledBrowsers":
                res = parser.handle_InstalledBrowsers(file)

            if path.split(".txt")[0] == "InstalledSoftware":
                res = parser.handle_InstalledSoftware(file)

            if path.split(".txt")[0] == "Passwords":
                res = parser.handle_Passwords(file)

            if path.split(".txt")[0] == "UserInformation":
                res = parser.handle_UserInformation(file)

            DATA[path.split(".txt")[0]] = res

    db.insert_data("data", DATA)
