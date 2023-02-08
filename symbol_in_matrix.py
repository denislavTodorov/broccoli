n =int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))
result = None
symbol = input()
for i in range(n):
    for j in range (n):
        if matrix[i][j] == symbol:
            result = f"({int(i)}, {int(j)})"
            break
    if result:
        break

if result:
    print(result)
else:
    print(f"{symbol} does not occur in the matrix")
