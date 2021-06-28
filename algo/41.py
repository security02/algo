x, y, z = map(float, input().split())
mn = min(x, y, z)
if x < 1 and y < 1 and z < 1:
    if mn == x:
        x = (y + z) / 2
    elif mn == y:
        y = (x + z) / 2
    else:
        z = (x + y) / 2
print(x, y, z)