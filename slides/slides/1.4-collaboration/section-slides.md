---
layout: section
---

# Python Skills for Collaboration

<v-click>

## Or How To Kill Project Velocity
</v-click>

<v-click>

### And How To Get It Back
</v-click>

---

## What We Will Learn

- How to Grind to a Halt
- Create Good Dev Experience
- Some Common Pitfalls

---

## Dependency Management Nightmare

What's the DevEx here?

```toml
# pyproject.toml
[project]
name = "mytool"
dependencies = []
```
```python
# src/analysis.py
import numpy as np
```

```python
# src/main.py
import typer
from . import analysis
```

<v-click>

Rince and repeat:
```bash
$ mytool
ImportError: typer
$ pip install typer && mytool
ImportError: numpy
```
</v-click>

---
layout: fact
---

Contributions to "mytool" welcome!

<v-click>

Excited to get started?
</v-click>

---

## Could have been worse

````md magic-move
```python
# src/analysis.py
import numpy

def calclate():
  ...
```

```python
# src/analysis.py
def calculate(*args, **kwargs): # <- cli entry point
  try:
    import cupy # <- use GPU acceleration if possible
    from ._cupy_calc import run
  except ImportError:
    from ._numpy_calc import run # <- fallback

  return run(*args, **kwargs)
```
````

<v-click at="2">you can</v-click><v-click at="3"> &ne; you should</v-click>
<v-click at="4">

-- The Motto of every true Professional
</v-click>

---
layout: fact
---

## Let's Fix This

<a href="https://github.com/eth-cscs/swe4py">https://github.com/eth-cscs/swe4py</a>

`exercises/1-4-collaboration/01-dependency-management`

---

## Packaging

Why make their life easy?

---
layout: two-cols
---

### Libraries without Packaging

<v-click>
Only ways to use:
</v-click>
<v-click>

- copy the code (and the dependencies)
</v-click>
<v-click>

- submodules
</v-click>
<v-click>

Who wouldn't want that?
</v-click>

::right::
### Packaged Libraries not on PyPi
<v-click>

Doable, however:
</v-click>
<v-click>

- Supply chain security concerns anyone?
</v-click>
<v-click>

- Not as pretty
</v-click>

---

### Easy to try out CLI App

````md magic-move
```bash
$ git clone git+https://github.com/DropD/mytool
$ cd mytool
$ uv venv .venv && source .venv/bin/activate
$ uv pip install -r requirements.txt
$ python run main.py
```

```bash
$ git clone git+https://github.com/DropD/mytool
$ cd mytool
$ uv run -s main.py # <- automatically installs deps
```

```bash
$ uvx run mytool-main --from "mytool @ https://github.com/DropD/mytool"
```

```bash
$ uvx run mytool-main --from mytool
```

```bash
$ uvx run mytool
```
````

<v-click at="1">

1. move dependencies to `pyproject.toml`
</v-click>
<v-click at="2">

2. Package (using `[project.script]`)
</v-click>
<v-click at="3">

3. Upload to PyPi
</v-click>
<v-click at="4">

4. Rename CLI to match distro
</v-click>

---

### Easy to try out & deploy web app

````md magic-move
```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ uv venv .venv && source .venv/bin/activate
$ uv pip install -r 
$ python manage.py collectstatic
$ python manage.py migrate
$ python manage.py loaddata example/fixtures.yml
$ python manage.py runserver
```

```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ uv run -s manage.py collectstatic # <- automatically installs deps
$ uv run -s manage.py migrate
$ uv run -s manage.py loaddata example/fixtures.yml
$ uv run -s manage.py runserver
```

```bash
$ git clone git+https://github.com/DropD/myapp
$ cd myapp
$ hatch run init # <- first time setup
$ hatch run dev # <- runs the dev server
```
````
<v-click at="1">

1. move dependencies to `pyproject.toml`
</v-click>
<v-click at="2">

2. use `hatch` tasks (or `pdm` or `uv` + a task runner)
</v-click>
<v-click at="3">

3. deploy expects "requirements.txt"?

`$ uv export > requirements.txt`
</v-click>
<v-click at="4">

No need to package or upload to PyPi
</v-click>
