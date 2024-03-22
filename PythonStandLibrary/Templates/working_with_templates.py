from string import Template
from pathlib import Path


template = Template(Path("template.html").read_text())
print(template.substitute({"name": "Emory.Du"}))
