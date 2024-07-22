# Integral Image

## Given an input image, calculating of the sum of pixels within a given rectangle using the Integral Image concept

### What is an *Integral Image*?

An *integral image* (or "summed-area table") is a data structure and algorithm for quickly calculating the sum of values in rectanguar subset of a grid

In this specific case, the script calculates the sum of pixels within a given rectangle, placed on the input image.

The concept of *integral image* is very useful in speeding up the calculation of Haar-like features. Infact, it works only with sum computations. Clearly, a sum computation is quicker than a product computation. 

The value at any point (*x*, *y*) in the *integral image* is the sum of all the pixels above and to the left of (*x*, *y*), inclusive.

Let's define some variables:

A = upper left corner of given rectangle 
B = upper right corner of given rectangle
C = bottom left corner of given rectangle
D = bottom right corner of given rectangle

z = sum of all the pixels within the given rectangle

Once the *integral image* for each point of the given rectangle (A, B, C, D) has been computed, the sum of pixels over the given rectangle must be computed. 

The sum of all the pixels within the given rectangle *z* is computed as:
z = I(D) + I(A) - I(B) - I(C)

where I(D) is the integral image computed for the D point, I(A) is the integral image computed for the A point etc...

Look at screenshots directory to see how the script works.
