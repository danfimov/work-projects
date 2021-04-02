# Task

Implement vector class that should make comparison of vectors by length – no non-standard libraries required.

**Warning:** Do not edit `test.py`

Usage:
```python
>>> Vector([1, 2])
Vector([1, 2])
```
it should raise an exeption if wrong input is given
```python
>>> Vector(1)
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].
```
```python
>>> Vector([[1]])
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].
```
```python
>>> Vector(["a"])
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].
```
```python
>>> Vector("a")
TypeError: expected Any[Tuple[Any[float, int]], List[Tuple[Any[float, int]]].
```
Compare vectors by length: `sqrt(1 ** 2 + 2 ** 2)` > `sqrt(0 ** 2 + 1 ** 2)`
```python
>>> Vector([1, 2]) > Vector([0, 1])
True
```
Vectors with the same length should be equal
```python
>>> Vector([1, 2]) >= Vector([2, 1])
True
```
```python
>>> Vector([1, 2]) <= Vector([2, 1])
True
```
You can't compare vectors with different number of elements
```python
>>> Vector([1, 2, 3]) >= Vector([2, 1])
ValueError: vectors shape mismatch.
```
If the difference between lengths of vectors is smaller than `EPSILON` (given in `task.py`) vectors are considered equal
```python
>>> Vector([1, 2]) == Vector([2, 1.00001])
True
```

Additional code requirements:
- types definition: `mypy task.py`
- pycodestyle: `pycodestyle task.py --max-line-length=120`
- [docstrings – in Google format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html): `darglint --docsting-style google task.py` 
- architecture
