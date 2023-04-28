

import json 
import argparse


def format_notebook(filename:str)->int:
    keys = ["outputs_hidden", "source_hidden"]
    retv = 0
    with open(filename, 'r') as f:
        data = json.load(f)
        for cell in data["cells"]:
            metadata = cell["metadata"]
            for key in keys:
                if "tags" in metadata.keys():
                    if key in metadata["tags"]:
                        if "jupyter" in metadata.keys():
                            if key in metadata["jupyter"].keys():
                                if metadata["jupyter"][key] == False: 
                                    metadata["jupyter"][key] = True 
                                    retv = 1
                            else:
                                metadata["jupyter"][key] = True
                                retv = 1
                        else:
                            metadata["jupyter"] = {key: True}
                            retv = 1
    if retv == 1:
        with open(filename, 'w') as f:
            json.dump(data, f)
    return retv



def main(argv = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= format_notebook(filename)
    return retv


if __name__ == '__main__':
    raise SystemExit(main())