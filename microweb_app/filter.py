import json
fname = 'beau.json'
with open (fname, "r") as file:
    docker_json = file.read()
    # print(docker_json)
    # print(type(docker_json))
    docker_dict = json.loads(docker_json)
    #print(type(docker_dict))
    #print(len(docker_dict))
    Container_ID = docker_dict[0]["Id"][0:5]
    print(Container_ID)
    Datum_Created = docker_dict[0]["Created"]
    print(Datum_Created)
    Status = docker_dict[0]["State"]["Status"]
    print(Status)
    Name_Container = docker_dict[0]["Name"]
    print(Name_Container)
    Host_Port = docker_dict[0]["HostConfig"]["PortBindings"]["5555/tcp"]
    print(Host_Port)
    Host_Name = docker_dict[0]["Config"]["Hostname"]
    print(Host_Name)
    IP_Address = docker_dict[0]["NetworkSettings"]["IPAddress"]
    print(IP_Address)
    MAC_Address = docker_dict[0]["NetworkSettings"]["MacAddress"]
    print(MAC_Address)
    print(docker_dict[0].keys())