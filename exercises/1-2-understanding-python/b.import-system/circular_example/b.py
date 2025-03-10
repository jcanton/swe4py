## -- b.py --
# b.py is being loaded

import a

CONSTANT_B = 42

def function_b(x):
    return x + a.function_a(x)

# b.py load has finished
