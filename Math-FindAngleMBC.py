# ABC is a right triangle, 90° at ∟ABC.
# Therefore, .

# Point M is the midpoint of hypotenuse AC.

# You are given the lengths AB and AC.
# Your task is to find ∠MBC (angle θ°, as shown in the figure) in degrees.

# Input Format

# The first line contains the length of side AB.
# The second line contains the length of side BC.


# Output Format

# Output  in degrees.

# Note: Round the angle to the nearest integer.

# Examples:
# If angle is 56.5000001°, then output 57°.
# If angle is 56.5000000°, then output 57°.
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10

# Sample Output

# 45°

from math import sqrt, acos, degrees

AB = int(input())

BC = int(input())

AC = sqrt(AB**2 + BC**2)

MC = AC/2

MBC = acos(BC/AC)

print(round(degrees(MBC)), '\u00B0',sep='')