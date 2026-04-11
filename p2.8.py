#8  Write a program to demonstrate that tuple is immutable.

colors = ("red", "blue", "green")
try:
    colors[0] = "yellow"
except TypeError:
    print("Cannot change tuple! It is immutable.")
