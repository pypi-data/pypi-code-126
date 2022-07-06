from pathlib import Path
import os

names = [
    ("promtail-local-config-linux1.yaml", "1"),
    ("promtail-local-config-linux2.yaml", "2"),
]

cwd = os.getcwd()
print (cwd)

template = Path('promtail-local-config-linux.yaml.template').read_text()

for filename, name in names:
    with open(filename, 'w') as outfile:
        outfile.write(template.format(name))
