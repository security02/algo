from math import pi
r1, r2, r3 = input().split()
r1 = int(r1)
r2 = int(r2)
r3 = int(r3)
s1 = pi*(r1**2)
s2 = pi*(r2**2)
s3 = pi*(r3**2)
print('%.2f %.2f %.2f' % (s1, s2, s3))
print('%.2f %.2f' % (s1, s2))



