import xml.etree.ElementTree as ET

def parse_schematic(file_source):

    tree = ET.parse(file_source)
    root = tree.getroot()

    schematic = root.find("drawing/schematic")

    if schematic is None:
        raise ValueError("Invalid EAGLE schematic structure")

    parts_element = schematic.find("parts")
    parts_data = []

    if parts_element is not None:
        for part in parts_element:
            parts_data.append({
                "reference" : part.attrib.get("reference"),
                "library" : part.attrib.get("library"),
                "deviceset" : part.attrib.get("deviceset"),
                "device" : part.attrib.get("device"),
                "value" : part.attrib.get("value", ""),
            })

    nets_data = []

    sheets = schematic.find("sheets")

    if sheets is not None:
        for sheet in sheets.findall("sheet"):
            nets_element = sheet.find("nets")

            if nets_element is None:
                continue

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
    return{
        "parts" : parts_data,
        "nets" : nets_data
    }