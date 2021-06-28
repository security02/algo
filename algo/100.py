from math import  *
x,y,c,d=map(int,input().split())
s=0
for a in range(1, x + 1):
    s+=(a*x+4)/(a+log(6))**(1/2)
print('%.2f' % s)
p=1
for a in range(1,y+1):
    p*=(a*x**2+6)/sin(a*x)
print('%.2f' % p)
for i in range(1,c+1):
    pp=1
    for j in range(1,d+1):
        pp*=(j*i+y*x)/((j*x+y)**(i/2))
print('%.2f' % pp)

