import json
import datetime


with open("name.json") as obj:
    data = json.load(obj)

    for x in data["imdata"]:
        day = x["l1PhysIf"][ "attributes"]["modTs"][:10]
        dn = x["l1PhysIf"][ "attributes"]["dn"]
        descr = x["l1PhysIf"][ "attributes"]["descr"]
        speed = x["l1PhysIf"][ "attributes"]["speed"]
        mtu  = x["l1PhysIf"][ "attributes"]["mtu"]
        d = datetime.date.fromisoformat(day)
        d = d.strftime("%A")

        if d == "Friday":
            print(f"{dn}\t{descr}\t\t\t{speed}\t\t{mtu}")

        








