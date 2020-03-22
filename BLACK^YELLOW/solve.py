from PIL import Image
import base64
im = Image.open("Darlene.png")
height,width = im.size

black=[]
yellow=[]
a=""
b=""
for i in range(height):
	for j in range(width):
		if im.getpixel((i,j))==(255,255,0,255):
			yellow.append((i,j))
			b+=chr(j%256)
		if im.getpixel((i,j))==(0,0,0,255):
			black.append((i,j))
			a+=chr(j%256)
#print black
#print yellow
#print a
#print b

key ="123abc456wixandmix"
passwd=""
j=0
s="Rl1BCgsNUxVBHh0QQQoFHwUdX1cTCBFDR1oWBxsRAgsICBoLER4TDQcXRxVVFh0bCU4zJSAsdGB8MidCFEVBE1NLGzEQXTYeXl5fURU8YWVpAwFJEjFUA1o="
s=base64.b64decode(s)
for i in s:
	passwd+=chr(ord(i)^ord(key[j%len(key)]))
	j+=1
print passwd
