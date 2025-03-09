# 3. Import system

## Import Detective

Given the following Python package (in `./detective/`):
```
detective/
├── __init__.py    # Empty
├── clue.py        # Define a variable: evidence = "fingerprint"
└── inspector.py   # Your task: import the evidence variable
```

In `inspector.py`, try to import the `evidence` variable from `clue.py` using whatever import style in a way that works for both running the file as a script and importing it as a module inside the `detective` package.

### Hint
```bash
$ python detective/inspector.py     # Found evidence: fingerprint
$ python -m detective.inspector     # Found evidence: fingerprint
```

## Circular import example  (`./circular_example/`)

Given the example of a circular import from the slides saved in the `circular_example` folder, add `print()` statements to all modules to show when they are being loaded. Once you have added the print statements, run the main script to see the loading order of the modules, check that it matches your expectations and fix the import cycle as explained in the slides.

### Hint
```bash
$ python circular_example/main.py  # Print 'start loading' / 'end loading' messages for all modules
```
