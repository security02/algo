a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
if a>=b>=c:
    print(2*a,2*b,2*c)
else:
    print(abs(a),abs(b),abs(c))