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

A class `vtwo` that works as a two-dimensional vector over the real numbers. Tentative plans to add another class later for arbitrary-dimensional vectors as well.

A `vtwo` is represented as `(x,y)`. You can add vectors component-wise, scale using `vec.scale(constant)`, get the magnitude using `abs(vec)`, find the dot (or inner) product using `vec1.dot(vec2)`, as well as the 2D scalar cross product, `vec1.cross(vec2)` which returns v_1 x v_2.

Other methods include finding the angle in standard position: `vec.angle('r')` for radians or `vec.angle('d')` for degrees. You can also find the angle between two vectors: `vec1.angle('r', vec2)` (with similar support for `d`). You can project vectors using `vec1.proj(vec2)` which is the projection of `vec1` *onto* `vec2`.

Vectors also support the `frac` type. That is, in addition to the components `x` and `y` being `int` or `float`, they can also be `frac`. You can turn them directly by using `vec.asFrac()`, which returns another `vtwo` object where the components are `frac`.

Finally, you can take a vector and represent it in the complex plane using `vec.asComplex()` which returns a `Complex` object.

---

## 3D Vectors

A class `vthree` that works as a three-dimensional vector over all real numbers. A `vthree` is represented as `(x,y,z)`. The same `scale`, `abs`, and `dot` methods work in three dimensions. Of course, the `vec1.cross(vec2)` method returns another vthree object. I will add similar `angle` and `proj` methods for finding angles and projections later.

Support for `frac` type still on-going; of course, there is no `asComplex` method.

---

## Complex Numbers

A standard complex number class. You can do normal arithmetic operations (add, subtract, multiply, divide). Perhaps future diving into exponentation, but that gets a bit complicated.

Initiated by `Complex(Real, Imaginary = 0)` so you can just put in a real number so that it acts as a complex number. Arithmetic operations can interface with `int`, `float`, or `frac` types. (So, the hierarchy here is that if `int` or `float` interface with a `frac`, they become `frac`. If any of the below interface with `Complex`, they become `Complex`.

Supports magnitude and conjugation. Can convert to vector using `com.asVector()`. Similarly, can convert `Real` and `Imaginary` to `frac` types using `com.asFrac()`.

---

## Polynomials

A standard real-number polynomial class. You can do addition, subtraction, and multiplication. The multiplication operation supports scaling by an integer or float (full frac support coming later), or by another polynomial. You can also add a constant integer or float. So, if you have a polynomial `a`, then `a+poly([3])` and `a+3` return the same thing. 

Displays in the "Mathematica style" that looks like `1 + x^1 + -2x^2 + x^4` for clarity.

You can evaluate the polynomial at a certain value by doing `myPoly.eval(n)`.

---

## Graphics (in development)

I like to use the [Asymptote Vector Graphics](http://asymptote.sourceforge.net) language to create diagrams. I use it at work, and it's an absolutely fantastic language with a pretty intuitive way of drawing things. It does a lot of the work for you.

So, naturally, I would like to be able to implement it to draw figures based on at least the `vtwo` objects, and probably `Complex` objects. However, you would need to have an installation of Asymptote and a postScript viewer. (Asymptote comes with TeXLive if you have that. The standard PostScript viewer at least on Debian-based Linux distros is `gv`. It seems this is also available on Mac via `brew`, and I'm unsure about Windows.)

Here is a minimum working example for using Asymptote with `vtwo`. The general format is `vec1.draw(ctx, vec2)` which draws `vec1` on the asymptote context `ctx`, with origin `vec2`.

You can also use `vec.label(ctx, string, origin, direction)` where `string` is a valid LaTeX-type string defining the label text, origin is the origin of where you're drawing the vector (so you can label vectors arbitrarily), and direction is a cardinal direction. Currently the direction is relative to the mid-point of the vector.

```python
from mrmath import *

## Create vector objects
origin = vtwo(0,0)
vec1 = vtwo(3,4)
vec2 = vtwo(1,2)
vec3 = vec1 - vec2

## Create asymptote object
g = asy()
g.size(200)

## Draw vectors
vec1.draw(g, origin)
vec2.draw(g, origin)
vec3.draw(g, vec2)

## Label vec1 as \vec{a}
## Use a raw string r' ' to make sure slashes work
vec1.label(g, r'"$\vec{a}$"', origin, 'SE')
vec2.label(g, r'"$\vec{b}$"', origin, 'NW')
vec3.label(g, r'"$\vec{a}-\vec{b}$"', vec2, 'NW')

del g
```
The result is a pretty basic image: 

![alt text](https://github.com/rich1126/mrmath/blob/master/newVecAdd.png "Vector Addition")

If you want to interface more directly with Asymptote within a Python script, because you want to do anything beyond drawing and labeling vectors, check out some of the basics [here](https://artofproblemsolving.com/wiki/index.php/Asymptote_(Vector_Graphics_Language)). Theoretically everything you could want can be done via the `send` method in asymptote.py, but some of the main functions like `draw`, `label`, `fill`, and `path` are written as methods to make things about 15% easier.

Of course, at that point it's probably easier to directly write Asymptote code. But hey, sometimes it's good to have things in the same place.
