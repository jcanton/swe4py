# Python Package Installer In Action

```bash
$ cd /workspaces/swe4py/exercises/build-install/01-installer
````

Let's install the fastest installer (if not there yet)

```bash
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

It can also create virtualenvs (fast), so let's do that.

```bash
$ uv venv venv-inst
$ source venv-inst/bin/activate
```

Inspect the `venv-inst` folder and convince yourself it's not magic.

Now, let's install a package (pick your favorite if you like, but also install numpy)

```
(venv-inst) $ uv pip install numpy
(venv-inst) $ python -c "import numpy"
```

Again inspect the `venv-inst` folder, specifically the `site-packages/`.

Notice you have something like

```
numpy-x.y.x.dist-info
numpy/
numpy.libs/
```

There is only metadata for one **distribution**, but two python **packages**.

Next, let's do an editable install. To that end we first create a dummy package

```bash
(venv-inst) $ uv init --lib dummy
(venv-inst) $ uv pip install -e dummy
```

Check out your `site-packages`, there should be a `_dummy.pth` file. What's inside it?

By the way, why are environments not movable? Try the following

```bash
$ grep -rn "01-installer/venv-inst" venv-inst --exclude "*.pyc"
```

The path is hardcoded in a few places. Simple to change? What about hardcoded paths in binaries?
