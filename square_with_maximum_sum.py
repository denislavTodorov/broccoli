rows, cols = [int(x) for x in input().split()]
counter = 0
for i in range(97, 97 + rows):
    current_line = ""

    for j in range(97, 97 + cols):
        current_line += chr(i) + chr(j + counter) + chr(i) + " "

    counter += 1

    print("".join(current_line))
