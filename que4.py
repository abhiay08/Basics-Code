def generate_pattern():
    # Printing the first line of stars
    print("* * * * * *")
    
    # Printing the middle lines with numbers
    for i in range(4, 8):
        print("*", end=" ")
        for j in range(i, i + 4):
            print(j, end=" ")
        print("*")
    
    # Printing the last line of stars
    print("* * * * * *")

generate_pattern()
