import json
import os

from pathlib import Path

import wheel_inspect


def deps(args):
    wheel_dir = args.dir[0]
    output = args.input_file

    if "pip3_dependencies" not in output:
        output["pip3_dependencies"] = {}
    if "wheel" not in output["pip3_dependencies"]:
        output["pip3_dependencies"]["wheel"] = []

    for f in os.listdir(wheel_dir):
        if f.endswith('.whl'):
            fpath = Path(wheel_dir) / f
            wheel = wheel_inspect.inspect_wheel(fpath)
            package_name = wheel['dist_info']['metadata']['name']
            output["pip3_dependencies"]["wheel"].append(
                {
                    "module": package_name,
                    "input_file": fpath.as_posix()  # SOAR uses posix paths
                }
            )
    print(json.dumps(output, indent=4), file=args.output_file)
