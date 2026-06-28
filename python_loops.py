"""
Python Loops - Basic Examples
Author: Deon John
"""

# -----------------------------
# 1. FOR LOOP
# -----------------------------
print("FOR LOOP")
for i in range(1, 6):
    print(i)

print()

# -----------------------------
# 2. WHILE LOOP
# -----------------------------
print("WHILE LOOP")
i = 1
while i <= 5:
    print(i)
    i += 1

print()

# -----------------------------
# 3. DO-WHILE (Python Equivalent)
# -----------------------------
print("DO-WHILE (Python Equivalent)")
i = 1
while True:
    print(i)
    i += 1

    if i > 5:
        break

print()

# -----------------------------
# 4. NESTED LOOP
# -----------------------------
print("NESTED LOOP")
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)

print()

# -----------------------------
# 5. BREAK
# -----------------------------
print("BREAK")
for i in range(1, 11):
    if i == 6:
        break
    print(i)

print()

# -----------------------------
# 6. CONTINUE
# -----------------------------
print("CONTINUE")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print()

# -----------------------------
# 7. PASS
# -----------------------------
print("PASS")
for i in range(1, 6):
    if i == 3:
        pass
    print(i)

print()

# -----------------------------
# 8. LOOPING THROUGH A LIST
# -----------------------------
print("LIST LOOP")
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

print()

# -----------------------------
# 9. LOOPING THROUGH A STRING
# -----------------------------
print("STRING LOOP")
word = "Python"

for letter in word:
    print(letter)

print()

# -----------------------------
# 10. RANGE EXAMPLES
# -----------------------------
print("RANGE EXAMPLES")

print("range(5)")
for i in range(5):
    print(i)

print()

print("range(1, 6)")
for i in range(1, 6):
    print(i)

print()

print("range(2, 11, 2)")
for i in range(2, 11, 2):
    print(i)

print()

print("range(5, 0, -1)")
for i in range(5, 0, -1):
    print(i)
