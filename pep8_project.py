#!venv/bin/python3
"""pep8_project.py

Usage:
    pep8_project.py [-c|-s|-r|-f] [-v]

Options:
    -c      Count infractions
    -s      Show source for infractions
    -r      Show source for infractions and compliance sample
    -f      Show first infractions

    -v      Show verbose infraction detail
"""
import itertools
import platform
import subprocess
from pathlib import Path

from docopt import docopt

# TODO: If no venv: make venv and just install pycodestyle

path_here = Path(__file__).parent / Path(".")


def pycodestyle_path():
    if platform.system() == "Windows":
        return path_here / "venv/Scripts/pycodestyle.exe"
    else:
        return path_here / "venv/bin/pycodestyle"


def make_pycodestyle_command(opts=None, verbose=False):
    opts = opts if opts else []
    verbose = ["-v"] if verbose else []
    return list(itertools.chain([str(pycodestyle_path())], opts, verbose, str(path_here)))


args = docopt(__doc__)
if args["-c"]:
    cmd = make_pycodestyle_command(["--statistics", "-qq"], verbose=args["-v"])
elif args["-s"]:
    cmd = make_pycodestyle_command(["--show-source"], verbose=args["-v"])
elif args["-r"]:
    cmd = make_pycodestyle_command(["--show-source", "--show-pep8"], verbose=args["-v"])
elif args["-f"]:
    cmd = make_pycodestyle_command(["--first"], verbose=args["-v"])
else:
    cmd = make_pycodestyle_command(verbose=args["-v"])

if args["-v"]:
    print(f"Running {' '.join(arg for arg in cmd)}")

subprocess.run(cmd)
