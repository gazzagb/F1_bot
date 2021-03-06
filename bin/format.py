import os
from pathlib import Path

style = "'{based_on_style: pep8, column_limit: 120}'"
for file in Path(".").rglob("*.py"):
    print(file)
    os.system(f"isort {file} > /dev/null; yapf -i --style {style} {file} > /dev/null;"
              f"docformatter -i {file} > /dev/null")
