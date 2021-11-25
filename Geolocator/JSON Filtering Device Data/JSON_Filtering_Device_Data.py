rack_struc = {
    "rack": [
        {"device": {"dev_id": "D1","dev_name": "R1","role": "router",
                   "interfaces": [
                       {"interface": "GigabitEthernet1", "ipaddress": "172.18.1.1", "subnet_mask": "255.255.255.0"},
                       {"interface": "GigabitEthernet2", "ipaddress": "172.18.3.1", "subnet_mask": "255.255.255.0"},
                       {"interface": "GigabitEthernet3", "ipaddress": "172.18.4.1", "subnet_mask": "255.255.255.0"}
                   ]
                }
        },
        {"device": {"dev_id": "D2","dev_name": "C1","role": "core",
                   "interfaces": [
                       {"interface": "VLAN1", "ipaddress": "172.18.1.2", "subnet_mask": "255.255.255.0"},
                       {"interface": "VLAN2", "ipaddress": "172.18.2.1", "subnet_mask": "255.255.255.0"},
                       {"interface": "VLAN20", "ipaddress": "172.18.20.1", "subnet_mask": "255.255.255.0"}
                   ]
                }
        },
        {"device": {"dev_id": "D3","dev_name": "AC","role": "access",
                   "interfaces": [
                       {"interface": "VLAN2", "ipaddress": "172.18.2.2", "subnet_mask": "255.255.255.0"},
                       {"interface": "VLAN3", "ipaddress": "172.18.3.3", "subnet_mask": "255.255.255.0"}
                   ]
                }
        }
    ]
}

import yaml
yaml_data = yaml.dump(rack_struc)
print(yaml_data)

# !pip install dicttoxml

from dicttoxml import dicttoxml
xml_data = dicttoxml(rack_struc)
print(xml_data)

import json
print('=======1=======')
print(type(rack_struc))
print(rack_struc)
#print('-------1-------')
js_struc = json.dumps(rack_struc)
#print(type(js_struc))
#print(js_struc)
#print(json.dumps(rack_struc, incident=8))

print('=======1B=======')
g = rack_struc["rack"][0]
print(type(g))
print(g["device"].keys())

print('=======2=======')
for g in rack_struc["rack"]:
    print('=======2A=======')
    print(type(g))
    print(g)
    print(g["device"]["dev_name"])
    for p in g["device"]["interfaces"]:
        print(p["ipaddress"])
        
print('=======3=======')
print("Keys device")
print(g["device"].keys())
print('=======3A=======')
print("Keys intefaces")
print(g["device"]["interfaces"][0].keys())

print('=======ALL-DEVICES-INTERFACES-IP-ADDRESSES=======')
for device in rack_struc["rack"]:
    print(device["device"]["dev_name"])
    for interface in device["device"]["interfaces"]:
        print(interface["interface"]+" => "+interface["ipaddress"])
