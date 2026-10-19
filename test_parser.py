from parser import parse_schematic

result = parse_schematic("sample.sch")

print("Total parts : ", len(result['parts']))
print("Total nets : ", len(result["nets"]))

print("\nParts : ")
for part in result["parts"]:
    print(part)

print("\nNets:")
for net in result["nets"]:
    print(net["name"], "->", net["connections"])