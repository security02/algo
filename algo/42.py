a,b,c,d = map(float, input().split())
if a <= b and b<= c  and c<= d:
    mx=max(a,b,c,d)
    a,b,c,d=mx,mx,mx,mx
else:
    mn=min(a,b,c,d)
    a,b,c,d=mn,mn,mn,mn
print(a,b,c,d)