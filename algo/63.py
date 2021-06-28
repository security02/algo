n=int(input())
S=0
P=1
for i in range(1,n+1):

    S+=(-1)**(i-1)/P
    P = P *(2*i+1)*(2*i)
print('%.4f' % S )