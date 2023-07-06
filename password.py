s = input("Enter your password: ")
capitalalphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
smallalphabets="abcdefghijklmnopqrstuvwxyz"
specialchar="$@_#%^&*()[\]{}|;:></?"
digits="0123456789"
a,b,c,d=0,0,0,0
if (len(s) >= 8):
	for i in s: 

		# counting lowercase alphabets
		if (i in smallalphabets): 
			a+=1		

		# counting uppercase alphabets
		elif (i in capitalalphabets): 
			b+=1	

		# counting digits
		elif (i in digits): 
			c+=1		

		# counting the mentioned special characters
		elif(i in specialchar): 
			d+=1 	
if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(s)):
	print("Valid Password")
	print("small alphabets are",a)
	print("capital alphabets are",b)
	print("digits are",c)
	print("special characters are",d)
else:
	print("Invalid Password")
