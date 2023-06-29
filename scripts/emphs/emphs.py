import re
import pyperclip

pattern: re.Pattern = re.compile(r"\\emph\{(?P<string>.*?)\}")


with open("scripts/emphs/emphs.txt", 'r') as file:
    content = file.read()

matches = set(pattern.findall(content))

matches.remove('Abfahrtsplan')
matches.remove('Klassen')

matches = sorted(list(matches))

for match in matches:
    print(match)
    pyperclip.copy(match)
    input()
    print()
    print()
