import argparse
import nbformat

def format_notebook(filename:str)->int:
    keys = ["outputs_hidden", "source_hidden"]
    retv = 0
    with open(filename, 'r') as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    for cell in nb["cells"]:
        metadata = cell["metadata"]
        print(metadata)
        for key in keys:
            if key in metadata.get("tags", []):
                jupyter_meta = metadata.setdefault("jupyter", {})
                before = jupyter_meta.get(key, False)
                if not before:
                    jupyter_meta[key] = True
                    retv = 1
    if retv == 1:
        with open(filename, 'w') as f:
            nbformat.write(nb, f, version=nbformat.NO_CONVERT)
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
