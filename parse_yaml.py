

import json 
from IPython import embed


keys = ["outputs_hidden", "source_hidden"]
with open('test_notebook.ipynb', 'r') as f:
    data = json.load(f)
    for cell in data["cells"]:
        metadata = cell["metadata"]
        for key in keys:
            if "tags" in metadata.keys():
                if key in metadata["tags"]:
                    if "jupyter" in metadata.keys():
                        metadata["jupyter"][key] = True 
                    else:
                        metadata["jupyter"] = {key: True}
with open('test_notebook.ipynb', 'w') as f:
    json.dump(data, f)
            # data['id'] = 134 # <--- add `id` value.
    # f.seek(0)        # <--- should reset file position to the beginning.
    # json.dump(data, f, indent=4)
    # f.truncate()     # remove remaining part