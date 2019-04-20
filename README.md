# mrmath

This holds some homemade classes and functions for various mathematical purposes. Nothing here is groundbreaking, or even particularly useful when compared to any modules available in Python. This is a hobbyist "Learn more Python" type project.

Navigate to the `mrmath` folder after downloading and run Python from there. Then just
``from mrmath import *``
to access all this has to offer.

---

## Fractions

A class called `frac` that acts as a common fraction.

`frac(a, b)` gives a common fraction of the form a/b, reduced to lowest terms.
If a single argument is given, `frac(a)`, it converts the float (or integer) into a fraction based on the decimal. So, `frac(1.25)` will return `5/4`.

Accepts addition, subtraction, multiplication, and division by another `frac`, as well as `int` and `float` types, returning a `frac` in each instance. Similarly, one can divide an `int` or `float` by a `frac` and get another `frac` in return.

Supports `float(myFrac)` to get its floating point representation. Naturally supports comparison, exponentiation (by an `int`, which returns a `frac`; or by a `float` or `frac` which returns a `float`.)

Has a simple method `myFrac.roundInt()` which just rounds it to the nearest integer. This is so `round()` method built-in to Python is not overloaded.

---

## 2D Vectors

A class `vtwo` that works as a two-dimensional vector over the real numbers. Tentative plans to add another class later for three-dimensional, then arbitrary-dimensional vectors as well.

A `vtwo` is represented as `(x,y)`. You can add vectors component-wise, scale using `vec.scale(constant)`, get the magnitude using `abs(vec)`, find the dot (or inner) product using `vec1.dot(vec2)`, as well as the 2D scalar cross product, `vec1.cross(vec2)` which returns v_1 x v_2.

Other methods include finding the angle in standard position: `vec.angle('r')` for radians or `vec.angle('d')` for degrees. You can also find the angle between two vectors: `vec1.angle('r', vec2)` (with similar support for `d`). You can project vectors using `vec1.proj(vec2)` which is the projection of `vec1` *onto* `vec2`.

Vectors also support the `frac` type. That is, in addition to the components `x` and `y` being `int` or `float`, they can also be `frac`. You can turn them directly by using `vec.asFrac()`, which returns another `vtwo` object where the components are `frac`.

Finally, you can take a vector and represent it in the complex plane using `vec.asComplex()` which returns a `Complex` object.

---

## Complex Numbers

A standard complex number class. You can do normal arithmetic operations (add, subtract, multiply, divide). Perhaps future diving into exponentation, but that gets a bit complicated.

Initiated by `Complex(Real, Imaginary = 0)` so you can just put in a real number so that it acts as a complex number. Arithmetic operations can interface with `int`, `float`, or `frac` types. (So, the hierarchy here is that if `int` or `float` interface with a `frac`, they become `frac`. If any of the below interface with `Complex`, they become `Complex`.

Supports magnitude and conjugation. Can convert to vector using `com.asVector()`. Similarly, can convert `Real` and `Imaginary` to `frac` types using `com.asFrac()`.
