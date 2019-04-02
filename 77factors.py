n=int(input())
x=""
for i in range(1,n+1):
	if n%i==0:
		x=x+" "+str(i)
		print(i)
