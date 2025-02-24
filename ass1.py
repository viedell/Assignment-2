# A, B and C

a = int(input("Input the number for A: "))

b = int(input("Input the number for B: "))

c = int(input("Input the number for C: "))



# Conditions

condition_1 = a > b or b > c

condition_2 = a % 2 == 0 and b % 2 != 0

condition_3 = b != c



# Condition boolean

if condition_1:

    print(f"Condition 1 met,", (int(a)), ">", (int(b)), "or", (int(b)), ">", (int(c)))

else:

    print(f"Condition 1 not met,", (int(a)), ">", (int(b)), "or", (int(b)), (int(c)))



if condition_2:

    print(f"Condition 2 met,", (int(a)), "is an even number and", (int(b)), "is an odd number.")

else:

    print(f"Condition 2 not met,", (int(a)), "is/not an even number and", (int(b)), "is/not an odd number.")



if condition_3:

    print(f"Condition 3 met,", (int(b)), "is not equal to", (int(c)))

else:

    print(f"Condition 3 not met,", (int(b)), "is equal to", (int(c)))



# If all conditions are met or not

if condition_1 and condition_2 and condition_3:

    print("All conditions are met!")

else:

    print("Not all of the conditions are met!")