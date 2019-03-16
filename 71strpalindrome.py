y=input()
if y.isalpha():
	y=y.casefold()
	x=reversed(y)
	if list(y)==list(x):
		print("yes")
	else:
		print("no")
else:
	print("no")
