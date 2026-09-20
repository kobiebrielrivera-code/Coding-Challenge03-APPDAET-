# Course: APPDAET
# Coding Challenge 03
# Challenge 03 - Linear System Analyzer
# Student Names: Aguilar, Bernal, Cabrera, Obille, Rivera
# Student Numbers: 12512293, 12512208, 12522896, 12512570, 12512769
# Section: BTIS1
# Date: September 20, 2026
# Program Purpose: To analyze a two-variable linear system by validating the input,
# computing determinants with Cramer's Rule,
# classifying the system and its geometry,
# and reporting a verified solution when one exists.


# TWO VARIABLE LINEAR SYSTEM ANALYZER
# a1x + b1y = c1
# a2x + b2y = c2

# INPUT
print("Enter coefficients for Equation 1 (a1x + b1y = c1):")
a1 = float(input("a1: "))
b1 = float(input("b1: "))
c1 = float(input("c1: "))

print("\nEnter coefficients for Equation 2 (a2x + b2y = c2):")
a2 = float(input("a2: "))
b2 = float(input("b2: "))
c2 = float(input("c2: "))

# VALIDATION
# An equation is invalid if BOTH variable coefficients are zero
eq1_valid = not (a1 == 0 and b1 == 0)
eq2_valid = not (a2 == 0 and b2 == 0)

if not eq1_valid or not eq2_valid:
    print("\n" + "=" * 50)
    print(" TWO-VARIABLE LINEAR SYSTEM ANALYZER")
    print("=" * 50)
    print("INVALID INPUT")
    if not eq1_valid:
        print("Equation 1 is invalid: both a1 and b1 are zero.")
    if not eq2_valid:
        print("Equation 2 is invalid: both a2 and b2 are zero.")
    print("This does not represent a valid linear equation in x and y.")
    print("=" * 50)

else:
    # INTERMEDIATE CALCULATION
    # Cramer's Rule determinants
    D = a1 * b2 - a2 * b1
    Dx = c1 * b2 - c2 * b1
    Dy = a1 * c2 - a2 * c1

    # DECISION LOGIC AND CLASSIFICATION
    if D != 0:
        classification = "CONSISTENT AND INDEPENDENT"
        solutions_text = "ONE UNIQUE SOLUTION"
        geometry_text = "The lines intersect."
    elif D == 0 and Dx == 0 and Dy == 0:
        classification = "CONSISTENT AND DEPENDENT"
        solutions_text = "INFINITELY MANY SOLUTIONS"
        geometry_text = "The equations describe the same line."
    else:
        classification = "INCONSISTENT"
        solutions_text = "NO SOLUTION"
        geometry_text = "The lines are parallel and distinct."

    # Only calculate solution and verify when D != 0
    if D != 0:
        x = Dx / D
        y = Dy / D

        # Verification by substitution
        L1 = a1 * x + b1 * y
        L2 = a2 * x + b2 * y
        check1 = "PASSED" if round(L1, 2) == round(c1, 2) else "FAILED"
        check2 = "PASSED" if round(L2, 2) == round(c2, 2) else "FAILED"

    # DISPLAY/ FINAL RESULT
    print("\n" + "=" * 50)
    print(" TWO-VARIABLE LINEAR SYSTEM ANALYZER")
    print("=" * 50)
    print("EQUATION 1")
    print(f"{a1:.2f}x + {b1:.2f}y = {c1:.2f}")
    print("\nEQUATION 2")
    print(f"{a2:.2f}x + {b2:.2f}y = {c2:.2f}")

    print("-" * 50)
    print("DETERMINANT ANALYSIS")
    print("-" * 50)
    print(f"D = {D:.2f}")
    print(f"Dx = {Dx:.2f}")
    print(f"Dy = {Dy:.2f}")

    print("-" * 50)
    print("SYSTEM CLASSIFICATION")
    print("-" * 50)
    print(f"Classification: {classification}")
    print(f"Number of Solutions: {solutions_text}")
    print(f"Geometric Interpretation: {geometry_text}")

    if D != 0:
        print("-" * 50)
        print("SOLUTION")
        print("-" * 50)
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
        print(f"Intersection Point: ({x:.2f}, {y:.2f})")

        print("-" * 50)
        print("VERIFICATION")
        print("-" * 50)
        print(f"Equation 1: {a1:.2f}({x:.2f}) + {b1:.2f}({y:.2f}) = {L1:.2f} {check1}")
        print(f"Equation 2: {a2:.2f}({x:.2f}) + {b2:.2f}({y:.2f}) = {L2:.2f} {check2}")

    print("=" * 50)