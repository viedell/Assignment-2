# X and Y

x = input("Enter value for x: ")

y = input("Enter value for y: ")



# Convert boolean

bool_x = bool(x)

bool_y = bool(y)



# Logical operations

andresult = bool_x and bool_y

orresult = bool_x or bool_y

notxresult = not bool_x

xorresult = (bool_x and not bool_y) or (not bool_x and bool_y)  # Logical XOR



# Print

print("Logical Operations Results:")

print(f"x: {x} > {bool_x}")

print(f"y: {y} > {bool_y}")

print(f"x AND y: {andresult}")

print(f"x OR y: {orresult}")

print(f"NOT x: {notxresult}")

print(f"x XOR y: {xorresult}")



print("-" * 25)



# Test Cases

test_cases = [

    (0, 0),

    (0, 1),

    (1, 0),

    (1, 1),

    ("", ""),

    ("", "Hello"),

    ("Python", ""),

    ("Python", "Hello"),

    (None, None),

    (None, 1),

    (None, "Test"),

]



print("Running Test Cases...")

for a, b in test_cases:

    bool_a, bool_b = bool(a), bool(b)

    xortest = (bool_a and not bool_b) or (not bool_a and bool_b)

    print(f"x = {a} ({bool_a}), y = {b} ({bool_b}) > XOR: {xortest}")