import json
import os

from pathlib import Path

import wheel_inspect


def deps(args):
    wheel_dir = args.dir[0]
    output = args.input_file

    if args.change_directory:
        os.chdir(args.change_directory)
    if not os.path.isdir(wheel_dir):
        raise NotADirectoryError(f"{wheel_dir} is not a directory")
    if args.pip3:
        pip_dependencies = "pip3_dependencies"
    else:
        pip_dependencies = "pip313_dependencies"
    if pip_dependencies not in output:
        output[pip_dependencies] = {}
    if "wheel" not in output[pip_dependencies]:
        output[pip_dependencies]["wheel"] = []

    for f in os.listdir(wheel_dir):
        if f.endswith('.whl'):
            fpath = Path(wheel_dir) / f
            wheel = wheel_inspect.inspect_wheel(fpath)
            package_name = wheel['dist_info']['metadata']['name']
            output[pip_dependencies]["wheel"].append(
                {
                    "module": package_name,
                    "input_file": fpath.as_posix()  # SOAR uses posix paths
                }
            )
    print(json.dumps(output, indent=4), file=args.output_file)
