'''
Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------
topology/pod-1/node-201/sys/phys-[eth1/33]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/34]                              inherit   9150 
topology/pod-1/node-201/sys/phys-[eth1/35]                              inherit   9150 
'''
import json

print("Interface Status\n================================================================================")
print("DN                                                 Description           Speed         MTU  ")
print("-------------------------------------------------- --------------------  ------       ------")

with open("name.json") as obj:
    data = json.load(obj)
    for x in data["imdata"]:
        dn = x["l1PhysIf"][ "attributes"]["dn"]
        descr = x["l1PhysIf"][ "attributes"]["descr"]
        speed = x["l1PhysIf"][ "attributes"]["speed"]
        mtu  = x["l1PhysIf"][ "attributes"]["mtu"]

        print(f"{dn}\t{descr}\t\t\t{speed}\t\t{mtu}")

