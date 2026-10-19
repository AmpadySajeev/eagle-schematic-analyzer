import xml.etree.ElementTree as ET

tree = ET.parse("sample.sch")
root = tree.getroot()


schematic = root.find('drawing/schematic')

part_elemets = schematic.find("parts")
parts_data = []

for part in part_elemets:
    parts_data.append({
        "reference" : part.attrib.get("name"),
        "library" : part.attrib.get("library"),
        "deviceset" : part.attrib.get("deviceset"),
        "device" : part.attrib.get("device"),
        "value" : part.attrib.get("value", "")
    })

sheets = schematic.find("sheets")
sheet = sheets.find("sheet")
nets_element = sheet.find("nets")

nets_data = []

for net in nets_element:
    connections = []

    for segment in net.findall("segment"):
        for pinref in segment.findall("pinref"):

            connections.append({
                "part" : pinref.attrib.get("part"),
                "pin" : pinref.attrib.get("pin")
            })

    nets_data.append({
        "name" : net.attrib.get("name"),
        "connections" : connections
    })

print("PARTS : ")
for part in parts_data:
    print(part)

print("\nNets : ")
for net in nets_data:
    print(net)            
        