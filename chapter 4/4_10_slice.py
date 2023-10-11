cubes = [i**3 for i in range(1, 11)]
for cube in cubes:
    print(cube)

print(f"first three items are: {cubes[:3]}")
print(len(cubes))
print(f"three middle items are: {cubes[3:5]}")
print(f"last three items are: {cubes[-3:]}")
