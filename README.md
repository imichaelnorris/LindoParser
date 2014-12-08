This project was an attempt to create an easy parser to write Python code that generates Lindo code.  I was required to use Lindo for a class project for a Linear Methods of Operations Research class, but I wasn't happy with the verbosity of the language, the structure of the language, or the limitations of the Free version of the language, so I wrote this script that allows you to write equations with variables, like 3*i < 45, and have them converted into an appropriate Lindo format for usage in its algorithm.

Simplex Method
==============
All equations are constraints for a Linear Optimization problem.
Variables either have a value or are symbolic.
Variables cannot be on the right side of an equation (balanacing constraint)
