import nbformat
from nbformat import read
import re
import os

current_dir = os.path.dirname(__file__)

notebook_path = os.path.join(current_dir, 'plot.ipynb')
requirements_path = os.path.join(current_dir, 'requirements.txt')

with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook = read(f, as_version=4)

imports = set()
for cell in notebook.cells:
    if cell.cell_type == 'code':
        code = cell.source
        # Find all import statements
        matches = re.findall(r'^\s*(?:import\s+(\w+)|from\s+(\w+)\s+import\s+\w+)', code, re.MULTILINE)
        for match in matches:
            # Add the module name to the set
            imports.update(filter(None, match))

with open(requirements_path, 'w', encoding='utf-8') as f:
    for imp in sorted(imports):
        f.write(f'{imp}\n')

print(f'Requirements have been written to {requirements_path}')