# Copyright (C) 2023 Jørgen S. Dokken and Benjamin Ragan-Kelley
#
# SPDX-License-Identifier:    MIT

import argparse

import nbformat


def format_notebook(filename: str) -> int:
    """
    Format a notebook with extra Jupyterlab tags, making it possible
    to collapse input and output when opening the file
    """
    tag_map = {
        "hide-input": "source_hidden",
        "hide-output": "outputs_hidden",
        "source_hidden": "source_hidden",
        "outputs_hidden": "outputs_hidden",
    }
    retv = 0
    with open(filename, "r") as f:
        nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)

    for cell in nb["cells"]:
        metadata = cell["metadata"]
        for key in tag_map.keys():
            if key in metadata.get("tags", []):
                jupyter_meta = metadata.setdefault("jupyter", {})
                before = jupyter_meta.get(tag_map[key], False)
                if not before:
                    jupyter_meta[tag_map[key]] = True
                    retv = 1

    if retv == 1:
        with open(filename, "w") as f:
            nbformat.write(nb, f, version=nbformat.NO_CONVERT)
    return retv


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("filenames", nargs="*")
    args = parser.parse_args(argv)

    retv = 0
    for filename in args.filenames:
        retv |= format_notebook(filename)
    return retv


if __name__ == "__main__":
    raise SystemExit(main())
