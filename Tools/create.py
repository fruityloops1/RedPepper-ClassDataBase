from lib import write
import sys

if len(sys.argv) != 2:
    print("create.py <class name>")
    sys.exit(1)

newClassName = sys.argv[1]

new = {'ClassName': newClassName, 'ClassNameFull': newClassName, 'Name': " ", 'Description': None, 'DescriptionAdditional': None, 'Args': None, 'Switches': None}
write(new, f"Data/{newClassName}.yml")