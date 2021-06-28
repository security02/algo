x,y=input().split()
x=int(x)
y=int(y)
if x!=y:
    if x>y:
        print({2*x*y},{(x+y)/2})
    else: print({(x+y)/2},{2*x*y})