#!venv/bin/python3
"""pep8_project.py

Usage:
    pep8_project.py [-c|-s|-r|-f]

Options:
    -c      Count infractions
    -s      Show source for infractions
    -r      Show source for infractions and compliance sample
    -f      Show first infractions
"""
import subprocess
from pathlib import Path

from docopt import docopt

# TODO: Make cross-platform
# TODO: If no venv: make venv and just install pycodestyle

path_here = Path(__file__).parent / Path(".")

args = docopt(__doc__)
if args["-c"]:
    subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                    "--statistics", "-qq",
                    "--max-line-length=119", str(path_here)])
elif args["-s"]:
    subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                    "--show-source",
                    "--max-line-length=119", str(path_here)])
elif args["-r"]:
    subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                    "--show-source", "--show-pep8",
                    "--max-line-length=119", str(path_here)])
elif args["-f"]:
    subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                    "--first",
                    "--max-line-length=119", str(path_here)])
else:
    subprocess.run(["venv/Scripts/pycodestyle", "--exclude=venv,migrations",
                    "--max-line-length=119", str(path_here)])
