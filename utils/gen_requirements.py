"""Manage requirements across the different submodules."""
import os
from pathlib import Path

requirements = set()
for filename in Path("book", "replications").rglob("requirements.txt"):
    requirements.update(
        map(lambda x: x.split("==")[0].lower(), filename.read_text().split())
    )

Path("requirements.txt").write_text(os.linesep.join(sorted(requirements)) + os.linesep)
