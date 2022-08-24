#queries=["+2", "+2", "+4", "+3", "-2"]
queries=["+4", "+5", "+2", "-4"]
diff=1
final=[]
arr=[]
for i,j in queries:
    t=0
    if i=="+":
        arr.append(int(j))
    else:
        while True:
            if int(j) not in arr:
                break
               
            arr.remove(int(j))
    if len(arr)>0:
        res = [(a, b) for idx, a in enumerate(arr) for b in arr[idx + 1:]]
        for a,b in res:
            if abs(a-b)==diff:
                t+=1
            
    final.append(t)
                
print(final)