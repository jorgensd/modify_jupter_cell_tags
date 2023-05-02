# test_local_precommit
Test a local precommit hook for jupyter notebook.

## Installation

Precommit can be install via `pip`;
```bash
python3 -m pip install pre-commit
```

## Update hook version
Check the source for the pre-commit hook and update them in [the config file](.pre-commit-config.yaml).
```bash
pre-commit autoupdate
```

## Run pre-commit