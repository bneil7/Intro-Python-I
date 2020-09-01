"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string 
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:
# x is 10, y is 2.25, z is "I like turtles!"
print("x is %d, y is %.2f, z is \"%s\"" % (x, y, z), "~~ printf (%) operator")

# Use the 'format' string method to print the same thing
data = (10, 2.25, "I like turtles!")
format_string = "x is %s, y is %s, z is \"%s\""
print(format_string % data, "~~ format string method")

# Finally, print the same thing using an f-string
print(f"x is {x}, y is {y:.2f}, z is \"{z}\"", "~~ f-string method")
