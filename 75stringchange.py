q=input()
z=len(q)
if z%2!=0:
    q=q[:int(z/2)]+'*'+q[int(z/2)+1:z]
else:
    q=q[:int(z/2)-1]+'**'+q[int(z/2)+1:z]
print(q)
