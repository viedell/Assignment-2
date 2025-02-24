# A for integer, B for string and C for float

a = int(input("Input any integer: "))

b = str(input("Input any string: "))

c = float(input("Input any float: "))



# Print out if it's correct or not

if isinstance(a, int) and isinstance(b, str) and isinstance(c, float):

    print(f"You put it all right! You type:", a, "for integer,", b, "for string and", c, "for float!")

else:

    print(f"You put it all wrong! You type:", a, "for integer,", b, "for string and", c, "for float!")



print("-" * 25)

# Testing

def checkinputtypes(a, b, c):



    
    if isinstance(a, int) and isinstance(b, str) and isinstance(c, float):

        return "Valid input types"

    else:

        return "Invalid input types"



 # Test Cases

print(checkinputtypes(10, "Hello", 69.0), "- Integer, string and float")

print(checkinputtypes("Hello", 10, 4.20), "- String, integer and float (Incorrect, should be int, str, float)")

print(checkinputtypes(5, "Test", 2), "- Integer, string and integer (3rd one should be float)")

print(checkinputtypes(20, "Python", 36.0), "- Integer, string and float")

print(checkinputtypes(5.5, 10, "String"), "- Float, integer, and string (Incorrect, should be int, str, float)")
