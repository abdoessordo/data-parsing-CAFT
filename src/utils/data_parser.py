
from traceback import print_tb


class parser:
    def get_folder_id(filename: str) -> str:
        return filename.split("[")[1].split("]")[0]

    def get_folder_region(filename):
        return filename.split("[")[0]

    def handle_ImportantAutofills(filename):
        DATA = {}
        with open(filename, "r") as f:
            res = f.read().split("\n")[5::]
            res.pop()
            for field in res:
                DATA[field.split(": ")[0]] = field.split(": ")[1]

        return DATA

    def handle_DomainDetects(filename):
        # DATA = {}
        # with open(filename, "r") as f:
        #     res = f.read().split("\n")[5::]
        #     return res
        pass

    def handle_InstalledBrowsers(filename):
        DATA = []
        with open(filename, "r") as f:
            res = f.read().split("\n")[5::]
            res.pop()
            for browser in res:
                browser = browser.split(") ")[1]
                browser_data = {}
                for field in browser.split(", "):
                    browser_data[field.split(": ")[0]] = field.split(": ")[1]
                DATA.append(browser_data)
        return DATA

    def handle_InstalledSoftware(filename):
        DATA = []
        with open(filename, "r") as f:
            res = f.read().split("\n")[5::]
            res.pop()
            for software in res:
                software = software.split(") ")[1]
                software_data = {
                    "name": software.split(" [")[0],
                    "version": software.split(" [")[1].split("]")[0],
                }
                DATA.append(software_data)

        return DATA

    def handle_Passwords(filename):
        DATA = []
        with open(filename, "r") as f:
            res = "\n".join(f.read().split("\n")[5::]).split("===============")
            for password in res:
                password_data = {}
                fields = [i for i in password.strip("\n").split("\n") if i]
                for field in fields:
                    password_data[field.split(": ")[0]] = field.split(": ")[1]
                if password_data != {}:
                    DATA.append(password_data)
        return DATA

    def handle_UserInformation(filename):
        pass
