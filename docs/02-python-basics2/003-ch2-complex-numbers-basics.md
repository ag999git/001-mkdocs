



### Beginners Guide to Complex Numbers in Python

Complex numbers let us work with quantities that have **two parts**:
- a **real part**
- an **imaginary part** (using **j** for √-1 in Python)

Example:
```python
z = 3 + 4j
```

#### Why complex numbers?
They are used in:
- electricity
- engineering
- signal processing
- physics
- computer graphics

---

#### How to create them
```python
z = 3 + 4j
w = complex(5, 2)   # same as 5 + 2j
```

---

#### Useful properties
```python
z.real      # real part
z.imag      # imaginary part
z.conjugate()
abs(z)      # magnitude
```

---

#### Basic operations
```python
z + w
z - w
z * w
z / w
```

---

##### Example
```python
z = 3 + 4j
print(z.real)        # 3.0
print(z.imag)        # 4.0
print(abs(z))        # 5.0
```

---

#### Summary
Complex numbers are simple in Python, built into the language, and very useful for engineering and science.



### Simple Guide to Complex Numbers in Python (Examples)

#### 1. Creating Complex Numbers

```python
print("5j ->", 5j)
# 5j

print("3 + 7j ->", 3 + 7j)
# (3+7j)

print("complex(10, -4) ->", complex(10, -4))
# (10-4j)

print("complex(6) ->", complex(6))
# (6+0j)
```

#### 2. Accessing Parts

```python
z = complex(10, -4)
print("z ->", z)
# (10-4j)

print("z.real ->", z.real)
# 10.0

print("z.imag ->", z.imag)
# -4.0

print("z.conjugate() ->", z.conjugate())
# (10+4j)
```

#### 3. Magnitude & Power

```python
print("abs(z) ->", abs(z))
# 10.770329614269007

print("pow(z, 2) ->", pow(z, 2))
# (84-80j)
```

#### 4. Arithmetic

```python
z1 = complex(10, -4)
z2 = complex(-3, 2)

print("z1 + z2 ->", z1 + z2)
# (7-2j)

print("z1 - z2 ->", z1 - z2)
# (13-6j)

print("z1 * z2 ->", z1 * z2)
# (-22+26j)

print("z1 / z2 ->", z1 / z2)
# (-2.2+1.6j)
```

#### 5. Unsupported Operations (Error Examples)

```python
# print(z1 // z2)  # TypeError
# print(z1 % z2)   # TypeError
# print(divmod(z1, z2))  # TypeError
# print(z1 > z2)   # TypeError
# print(z1 < z2)   # TypeError

print("z1 == z2 ->", z1 == z2)
# False
```

#### 6. Large Complex Numbers

```python
import sys

large = complex(5e12, -8e12)
print(sys.getsizeof(large))
# 32–48 bytes depending on Python version

print("large + large ->", large + large)
# (1e13-1.6e13j)

print("large - large ->", large - large)
# 0j

print("large * large ->", large * large)
# (-3.9e25-8e25j)

print("large / large ->", large / large)
# (1+0j)
```
