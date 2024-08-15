final_x=[]
final_y=[]

n = len(final_x)

e = [-1 for i in range(n)]

def find(v):
    if(e[v]<0):
        return v
    else:
        e[v]=find(e[v])
        return e[v]
    
def join(a,b):
    a=find(a)
    b=find(b)

    if(a==b):
        return 0

    if(e[a]>e[b]):
        temp=a
        a=b
        b=temp
    
    e[a]+=e[b]
    e[b]=a
    return 1

for i in range(n):
    for j in range(n):
        dist = (final_x[i]-final_x[j])**2+(final_y[i]-final_y[j])**2

        if(dist<10):
            join(i,j)
        
leaders = []

for i in range(n):
    if(e[i]<0):
        leaders.append(i)

groups = []

for i in range(len(leaders)):
    temp= []
    for j in range(n):
        if(find(j)==leaders[i]):
            temp.append(j)
    
    groups.append(temp)
