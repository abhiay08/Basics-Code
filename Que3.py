def generate_pattern():
    # First part of the pattern
    for i in range(1, 6):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()
    
    # Second part of the pattern
    for i in range(4, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

generate_pattern()
