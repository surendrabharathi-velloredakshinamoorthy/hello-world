text = input ("Enter string : \n")
text_length = len(text)
if (text_length < 3):
	print (text)
else:
	lastdigit = text[text_length-3] + text[text_length-2] + text[text_length-1]
	if lastdigit == "ing":
		print(text +"ly")
	else:
		print(text +"ing")
