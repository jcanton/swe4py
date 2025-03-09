## -- a.py --
# a.py is being loaded
import b

#print(f"At module `a` scope: {hasattr(b, 'CONSTANT_B')=}")
CONSTANT_A = b.CONSTANT_B + 10

def function_a(x):
    # CONSTANT_A = b.CONSTANT_B + 10  # Here is ok
    #print(f"Inside function: {hasattr(b, 'CONSTANT_B')=}")
    return x + CONSTANT_A

# a.py load has finished
