def search(my,ss):
	count = 0
	my = my.split()
	for i in range(0,len(my)):
		if ss == my[i]:
			count+=1
	if count == 0:
		print("no substing")
	else:
		print("substring found",count)

mystring = 'A geek in need is a geek indeed'
ss = input("enter substring to find")
search(mystring,ss)