# Course: APPDAET
# Coding Challenge 03
# Challenge 02 - Quadratic Analyzer
# Student Names: Aguilar, Bernal, Cabrera, Obille, Rivera
# Student Numbers: 12512293, 12512208, 12522896, 12512570, 12512769
# Section: BTIS1
# Date: September 20, 2026
# Program Purpose: To analyze a quadratic equation by validating the input,
# computing the discriminant and vertex,
# classifying the parabola and its roots,
# and presenting a clear report of the solutions and graph behavior.


# QUADRATIC EQUATION AND PARABOLA ANALYZER
# ax^2 + bx + c = 0

# This is the input
print("Enter coefficients for the quadratic equation (ax^2 + bx + c = 0):")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

# This is the validation
# An equation is not quadratic if the 'a' coefficient is zero
eq_valid = (a != 0)

if not eq_valid:
    print("\n" + "=" * 50)
    print(" QUADRATIC EQUATION AND PARABOLA ANALYZER")
    print("=" * 50)
    print("INVALID INPUT")
    print("The coefficient 'a' cannot be zero.")
    print("This does not represent a valid quadratic equation.")
    print("=" * 50)

else:
    # This is the intermidiate calculation
    # Discriminant formula: b^2 - 4ac
    discriminant = (b ** 2) - (4 * a * c)
    
    # Vertex coordinates formula: x = -b / 2a, y = plug x back into equation
    vertex_x = -b / (2 * a)
    vertex_y = a * (vertex_x ** 2) + b * vertex_x + c

    # This is the decision logic and classification
    # 1. Parabola Direction
    if a > 0:
        direction = "UPWARD"
        vertex_type = "MINIMUM"
    else:
        direction = "DOWNWARD"
        vertex_type = "MAXIMUM"

    # 2. Discriminant Classification
    if discriminant > 0:
        classification = "POSITIVE"
        roots_text = "TWO DISTINCT REAL ROOTS"
        geometry_text = "The parabola crosses the x-axis twice."
    elif discriminant == 0:
        classification = "ZERO"
        roots_text = "ONE REAL ROOT (REPEATED)"
        geometry_text = "The parabola's vertex rests exactly on the x-axis."
    else:
        classification = "NEGATIVE"
        roots_text = "TWO COMPLEX/IMAGINARY ROOTS"
        geometry_text = "The parabola does not touch or cross the x-axis."

    # Only calculate real roots when they exist
    if discriminant >= 0:
        root1 = (-b + (discriminant ** 0.5)) / (2 * a)
        root2 = (-b - (discriminant ** 0.5)) / (2 * a)

    # This is the part where the final result will be shown or printed.
    print("\n" + "=" * 50)
    print(" QUADRATIC EQUATION AND PARABOLA ANALYZER")
    print("=" * 50)
    print("EQUATION")
    print(f"{a:.2f}x^2 + {b:.2f}x + {c:.2f} = 0")

    print("-" * 50)
    print("PARABOLA PROPERTIES")
    print("-" * 50)
    print(f"Opening Direction: {direction}")
    print(f"Vertex Type: {vertex_type}")
    print(f"Vertex Coordinates: ({vertex_x:.2f}, {vertex_y:.2f})")

    print("-" * 50)
    print("DISCRIMINANT ANALYSIS")
    print("-" * 50)
    print(f"Discriminant Value: {discriminant:.2f}")
    print(f"Classification: {classification}")

    print("-" * 50)
    print("ROOTS CLASSIFICATION")
    print("-" * 50)
    print(f"Number of Solutions: {roots_text}")
    print(f"Geometric Interpretation: {geometry_text}")

    if discriminant > 0:
        print("-" * 50)
        print("SOLUTIONS")
        print("-" * 50)
        print(f"Root 1 (x1) = {root1:.2f}")
        print(f"Root 2 (x2) = {root2:.2f}")
        print(f"x-intercepts: ({root1:.2f}, 0) and ({root2:.2f}, 0)")
    elif discriminant == 0:
        print("-" * 50)
        print("SOLUTION")
        print("-" * 50)
        print(f"Root (x) = {root1:.2f}")
        print(f"x-intercept: ({root1:.2f}, 0)")

    print("=" * 50)
