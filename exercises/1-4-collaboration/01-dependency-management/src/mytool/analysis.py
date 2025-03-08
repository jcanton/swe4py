from __future__ import annotations
import typing


if typing.TYPE_CHECKING:
    import numpy


def calculate(a: int, b: int) -> numpy.NDarray:
    try:
        import cupy
        from ._cupy_calc import run
    except ImportError:
        from ._numpy_calc import run

    return run(a, b)
