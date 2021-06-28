a,b,c=map(int,input().split())
d=(b**2-4*a*c)**1/2
if a!=0 and d>0:
    x1=(-b+d)/(2*a)
    x2=(-b-d)/(2*a)
    print('%.2f' % x1,x2)
else: print('NO')