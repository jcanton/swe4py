# Fix Dependency Management

Currently, we would need to find all the dependencies by seeing what fails to import and check for hidden imports hidden in control flow.

Let's improve this by putting them all into the project's dependencies.

```toml
# pyproject.toml

[project]
...
dependencies = ["click", "numpy"]
...

[project.optional-dependencies]
gpu = ["cupy-cuda12x"]
```

Now it's a simple matter of

```bash
$ uv venv .venv && source .venv/bin/activate
(.venv) $ uv pip install -e .
```

Hang on, aren't we promising that this will work with every version of all our dependencies right now?

Yes. We might want to restrict that.

```toml
# pyproject.toml

[project]
...
dependencies = [
    "click >= 8.1.7",
    "numpy >= 1.26.4"
]
...

[project.optional-dependencies]
gpu = ["cupy-cuda12x >= 12.0"]
```

But what if another developer starts out later and get's a newer version with subtly different behavior, won't that make it difficult to reason about our code?

Yes. Our options not long ago:

1. pin the versions in `pyproject.toml`
2. pin the versions in a `requirements.txt`
  a) add a script to keep it up to date with `pyproject.toml`
3. maintain an official "dev container" fith fixed versions

We don't want to pin in `pyproject.toml`, because we hurt interoperabilityof our project. Option 1 is out.

A dev container does not reduce friction much for those who don't live in an IDE that can make use of it. Option 3 should only be complimentary.

Option 2a looks good, if we can all remember to regularly 
```bash
pip install -r requirements.txt
```
And of course we need to keep a separate file for optional packages.

Our options now:

```bash
$ uv lock
$ head uv.lock
```

`pdm` has equivalent functionality.

This creates a lock file, from which `uv` (or `pdm`) can read which version of which package it should use for development tasks like running tests (including transitive dependencies).

The lock file can also be used when deploying a service to ensure it has the same exact set of dependencies as in development.
