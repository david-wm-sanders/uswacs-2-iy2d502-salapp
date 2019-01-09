#!/usr/bin/env python3
import subprocess
from pathlib import Path

# TODO: Make cross-platform
# TODO: If no venv: make venv and just install pycodestyle
# TODO: Add some nice docopt

p = Path(__file__).parent / Path(".")
subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                "--show-source", "--max-line-length=119", str(p)])
