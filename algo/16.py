x,y=input().split()
x=float(x)
y=float(y)
a=abs((y**2+2)/(x+x**3/5))
c1=(x+y)/(y**2+a)+exp(y+2)
print('%.2f' % c1)