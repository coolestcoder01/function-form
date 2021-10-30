def print_list(list):
    for x in list:
        print(x)

my_list = ["tomato", "corn", "beets"]

print_list(my_list)

def generateCRC():
	code=list(map(int,input("Enter Code: ")))
	div=list(map(int,input("Enter Divisor: ")))
	rem=div.copy()
	for ctr in range(0,len(div)):
		rem[ctr]=code[ctr] ^ div[ctr]
		code.append(0)
	code=code[0:-1]
	for ctr in range(len(div),len(code)):
		remainder=rem.copy()
		remainder=remainder[1:]	#Removes the first 0
		remainder.append(code[ctr])
		while remainder[0]==0 and ctr<len(code)-1:	 #borrows one zero of next bit
			remainder=remainder[1:]
			ctr+=1
			remainder.append(code[ctr])
		if remainder[0]!=0:
			for t in range(0,len(div)):
				rem[t]=remainder[t] ^ div[t]
		ctr+=1
	return rem[1:]
