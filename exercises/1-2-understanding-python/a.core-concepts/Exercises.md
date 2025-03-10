# Core concepts exercises

## Global variable modification

The following code snippet defines a global variable `global_var` and a function `f` that modifies it. What do you expect the output to be when running the script?
Think about it and then run the script to check your answer.

```python
global_var = "start_value"

def f():
    global global_var
    global_var = "new_value"

print(f"{global_var=}")
f()
print(f"{global_var=}")
```
Given what you know about scopes read and write scopes, can you think of a simple way to modify the snippet so `global_var` could be modified inside the function without using the `global` keyword?


## Customizing class behavior

In Python the behavior of classes can be customized by defining special methods, also known as "magic methods" or "dunder methods". These methods are called by the Python interpreter in response to certain operations, like arithmetic operations, attribute access, etc. For example, the `__add__` method is called when the `+` operator is used with an instance of a class.

In Python there are also _in-place_ operators (`+=`, `*=`, ...) and their corresponding special methods (`__iadd__`, `__imul__`, ...). Let's check how does it work with a simple example with lists:

```python
a = [1]

print(hasattr(type(a), "__iadd__"))   # True
a += [2]  # Basically equivalent to: a.append(2)

print(a)  # [1, 2]

```

However, immutable types like `tuple` cannot be modified after creation and therefore do not have an `__iadd__` (or `.append()`) method, so the following code should raise an exception:

```python
a = (1,)

print(hasattr(type(a), "__iadd__"))  # False
a += (2,)

```
What happens? Why?


## Identity of objects

In Python, everything is an object, and objects have an identity, a type, and a value. The identity of an object is unique and constant for the lifetime of the object. The `id()` function returns the identity of an object. The `is` operator compares the identity of two objects.

```python
# Small integer
a = 1
print(a + 1 == a + 1)
print(a + 1 is a + 1)

# Large integer
a = 1234
print(a + 1 == a + 1)
print(a + 1 is a + 1)

# Float
import random
a = random.random()
print(a + 1 == a + 1)
print(a + 1 is a + 1)
```
Do they all return the same result? Why?

In the slides we defined the `is` operator as a comparison of the identities of the its arguments (`a is b` ~= `(id(a) == id(b)`), however, if you execute the following snippet several times, you might see weird behavior...
```python
class A:
    @property
    def foo(self):
        return object()


a = A()

id(a.foo) == id(a.foo), a.foo is a.foo
```
What happens? How would you explain it?


## Playing with `__getattr__` and missing attributes

Write a Python base class with a custom `__getattr__` method which, whenever a missing attribute is trying to be accessed, it returns the existing attribute with the most similar name (if any). The [`difflib.get_close_matches()`](https://devdocs.io/python~3.13/library/difflib#difflib.get_close_matches) function might be useful for this task. Start from the following code skeleton:

```python
import dataclasses
import difflib

class FuzzyAttributes:
    def __getattr__(self, attr):
    # Write a `__getattr__` method that returns the value of the attribute that
    #  is the closest to the requested attribute name (use
    #  `difflib.get_close_matches()`. If there is no attribute that is close
    #  enough, raise an `AttributeError`.

    raise AttributeError(attr)

@dataclasses.dataclass
class Person(FuzzyAttributeGetter):
    name: str
    age: int
    country: str
    income: int

p = Person("John Smith", 30, "USA", 50000)

print(p.name) # John Smith
print(p.nam)  # John Smith
print(p.ag)   # 30

print(p.asdfasdfdad3af)  # AttributeError

```
