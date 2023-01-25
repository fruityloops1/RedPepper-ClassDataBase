from lib import read
import sys

if len(sys.argv) != 2:
    print("create.py <class name>")
    sys.exit(1)

className = sys.argv[1]
data = read(f"Data/{className}.yml")

print(f"Class Name: {data['ClassNameFull']}")
print(f"Name: {data['Name']}")
if data['Description'] is not None:
    print(f"Description: {data['Description']}", end='')
if data['DescriptionAdditional'] is not None:
    print(f", {data['DescriptionAdditional']}")
else:
    print()

if data['Switches'] is not None:
    print("Switches:")
    for switch in data['Switches']:
        print(f"\t{switch}")


if data['Args'] is not None:
    print("Arguments:")
    i = 0
    for arg in data['Args']:
        print(f"\t{arg}:")
        
        curArg = data['Args'][arg]

        if 'Name' in curArg:
            print(f"\t\tName: {curArg['Name']}")
        if 'Description' in curArg:
            print(f"\t\tDescription: {curArg['Description']}")
        if 'Default' in curArg:
            print(f"\t\tDefault Value: {curArg['Default']}")
        if 'Required' in curArg:
            print(f"\t\tIs required: {curArg['Required']}")
        i += 1