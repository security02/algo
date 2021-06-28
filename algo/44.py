x,y,z=map(int,input().split())
if x>0 and y>0 and z>0:
    if x+y>z and x+z>y and z+y>x:
        print("YES")
    else: print('NO')
