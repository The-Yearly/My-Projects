x=["230","121","452","783","124","1213"]
print(x)
for g in range(0,len(x)):
    for y in range(0,len(x)-g-1):
        if x[y][2]>x[y+1][2]:
            x[y],x[y+1]=x[y+1],x[y]
print(x)
