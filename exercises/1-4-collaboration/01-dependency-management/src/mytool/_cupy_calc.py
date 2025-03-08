import cupy


def run(a: int, b: int) -> cupy.array:
    return cupy.array([a] * 3) + cupy.array([b] * 3)
