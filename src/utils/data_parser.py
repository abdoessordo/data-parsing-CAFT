from utils.helper import Helper

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
        DATA = []
        with open(filename, "r") as f:
            res = f.read().strip("\n").split("\n")
            for domains in res:
                if Helper.checkDomain(domains):
                    for domain in domains.split(", "):
                        domain_data = {}

                        domain_data["name"] = domain.split(
                            " ")[0].strip("]").strip("[")
                        domain_data["domain"] = domain.split(" ")[1]
                        DATA.append(domain_data)

        return Helper.ObjectSet(DATA)

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
        with open(filename, "r") as f:
            res = [part.strip("\n") for part in "\n".join(f.read().split("\n")[5::]).split('\n\n')]
            DATA = {}
            
            userInfo = {}
            for info in res[0].split("\n"):
                userInfo[info.split(": ")[0]] = info.split(": ")[1]
            
            keyboards = []
            for info in res[1].split("\n")[1::]:
                keyboard = {
                    "language": info.split(" ")[0],
                    "region": info.split(" ")[1].strip(")").strip("(")
                }
                keyboards.append(keyboard)
            
            hardwares = {}
            for i, info in enumerate(res[2].split("\n")[1::]):
                hardwares[f'{info.split(": ")[0]}_{i}'] = info.split(": ")[1].replace("   , ", ", ")


            anti_viruses = []
            for antivirus in res[3].split("\n")[1::]:
                anti_viruses.append(antivirus)

            print(anti_viruses)

            DATA["userInfo"] = userInfo
            DATA["keyboards"] = keyboards
            DATA["hardwares"] = hardwares
            DATA["anti_viruses"] = anti_viruses


        return DATA