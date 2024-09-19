n, m=map(int,input().split(' '))
heng=[]
yul=[]
max=0
min=[]

for i in range(n):
    heng=list(map(int,input().split()))
    yul.append(heng)

for i in range(n):
    a=yul[i][0]
    for j in range(m):
        if a>yul[i][j]:
            a=yul[i][j]
    min.append(a)

max=min[0]
for i in range(n):
    if max<min[i]:
        max=min[i]

print(max)
            
            
    