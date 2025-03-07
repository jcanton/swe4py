---
layout: section
---

# Environments & Package Installs

---

## What we will Learn

- Virtualenv Gotchas
- Why are environments not movable?
- What does a Package install do?
- Where can Packages come from?

---

## Gotchas

### 1. Package Managers

---

Does this work?

```bash
$ conda activate apple

(apple) $ pip install numpy
```
<v-click>

😄 Yes!
</v-click>

---

How about this?
```bash
$ source orange/bin/activate

(orange) $ conda install tensorflow
```

<v-click>

```bash {5}
Retrieving notices: ...working... done
...
## Package Plan ##
  environment location: /opt/anaconda3
```

Installs into base conda environment 😢 
Why?

</v-click>

---
layout: fact
---

Conda Env

&ne;

Virtualenv

---

What about this?
```bash
$ spack activate bananas
(bananas) $ spack install py-pip

(bananas) $ pip install numpy
```

<v-click>

<a href="https://github.com/spack/spack/issues/28282">Used to install into system environment in 2023 😢</a>

Also, pip might "upgrade" python packages you installed with spack.
</v-click>

---

But this works!

```bash
$ source venv/bin/activate
(venv) $ pip install uv
(venv) $ uv pip install jupyterlab
```

And `uv pip` is a lot faster.

They are both Python Package Managers

---

## Gotchas

### 2. Where is my Package?

---

Work on Project A
```bash
project_a $ source .venv/bin/activate
(.venv) project_a $ pip install rich, numpy
```
<v-click>

Work on Project B
```bash
(.venv) project_a $ deactivate
project_a $ cd ../project_b
(.venv) project_b $ source .venv/bin/activate
(.venv) project_b $ pip install numpy
```
</v-click>
<v-click>

Return to Project A
````md magic-move
```bash
(.venv) project_b $ cd ../project_a
(.venv) project_a $ python -c "import rich, numpy; rich.print(numpy.array([1, 2, 3]))"
raceback (most recent call last):
  File "<string>", line 1, in <module>
    import rich, numpy
ModuleNotFoundError: No module named 'rich'
```

```bash
(.venv) project_b $ deactivate
(.venv) project_b $ cd ../project_a && source .venv/bin/deactivate
(.venv) project_a $ python -c "import rich, numpy; rich.print(numpy.array([1, 2, 3]))"
[1 2 3]
```

````
</v-click>

---

How to not forget?

<v-click>

- Use `direnv` to automatically activate & deactivate
</v-click>
<v-click>

- Teach your IDE which env for which project (& never leave the IDE)
</v-click>
<v-click>

- Use `uv`, `hatch` or `pdm` to work on projects

```bash
project_a $ uv add rich, numpy
project_a $ cd ../project_b
project_b $ uv add numpy
project_b $ cd ../project_a
project_a $ uv run python -c "import rich, numpy; rich.print(numpy.array([1, 2, 3]))"
[1 2 3]
```

(This requires your projects to have a `pyproject.toml` file)
</v-click>

---

## Gotchas
### 3. Venvs don't stack

---

Activate "thisenv"
```bash
$ source thisenv/bin/activate
```
<v-click>
Activate "otherenv"
```bash
(thisenv) $ source otherenv/bin/activate
```
</v-click>
Deactivate "otherenv"
<v-click>
```bash
(otherenv) $ deactivate
```
</v-click>
<v-click>
```bash
$ which python
  #NOT thisenv/bin/python
```
</v-click>

---

## Anatomy of a Virtualenv

---

## Anatomy of a Package Install

---

## Exercises
