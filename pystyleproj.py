#!venv/bin/python3
"""pystyleproj.py

Usage:
    pystyle_proj.py [-c|-s|-r|-f] [-d] [-v]

Options:
    -c      Count infractions
    -s      Show source for infractions
    -r      Show source for infractions and compliance sample
    -f      Show first infractions

    -d      Include pydocstyle infractions
    -v      Show verbose infraction detail
"""
import itertools
import platform
import subprocess
from pathlib import Path

from docopt import docopt

# TODO: If no venv: make venv and just install pycodestyle

path_here = Path(__file__).parent / Path(".")


def pyxstyle_path(x, venv_dir="venv"):
    extension = ".exe" if platform.system() == "Windows" else ""
    bin_dir = "Scripts" if platform.system() == "Windows" else "bin"
    return [str(path_here / f"{venv_dir}/{bin_dir}/py{x}style{extension}")]


def make_pyxstyle_command(x, opts=None, verbose=False):
    opts = opts if opts else []
    verbose = ["-v"] if verbose else []
    return list(itertools.chain(pyxstyle_path(x), opts, verbose, str(path_here)))


args = docopt(__doc__)
if args["-c"]:
    cmds = [make_pyxstyle_command("code", ["--statistics", "-qq"], verbose=args["-v"])]
elif args["-s"]:
    cmds = [make_pyxstyle_command("code", ["--show-source"], verbose=args["-v"])]
elif args["-r"]:
    cmds = [make_pyxstyle_command("code", ["--show-source", "--show-pep8"], verbose=args["-v"])]
elif args["-f"]:
    cmds = [make_pyxstyle_command("code", ["--first"], verbose=args["-v"])]
else:
    cmds = [make_pyxstyle_command("code", verbose=args["-v"])]

for cmd in cmds:
    if args["-v"]:
        print(f"Running {' '.join(arg for arg in cmd)}")
    subprocess.run(cmd)
