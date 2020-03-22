# **MISC**

## BLACK^YELLOW:
![](/BLACK^YELLOW/Task.png)

link : https://gofile.io/?c=QoxGao


So we've got first a password protected zip file [part1.zip](/BLACK^YELLOW/part1.zip) and a png [Darlene.png](/BLACK^YELLOW/Darlene.png). From the task name we know we are going to work with those BLACK and YELLOW dots in the photo (you can spot them on the top-left corner):

![](/BLACK^YELLOW/Darlene.png) 

First thing let's print the coordinates of those pixels, We can see that the second value y of (x,y) seems to be chars ASCII code (not always though)

![](/BLACK^YELLOW/arrays.png)

if we try and print those values we get:

![](/BLACK^YELLOW/Strings.png)

We can see the first string seems to be base64 encoded and we can spot the seperator = , however it contains a non-ASCII chars. We get rid of those chars and get the first string *Rl1BCgsNUxVBHh0QQQoFHwUdX1cTCBFDR1oWBxsRAgsICBoLER4TDQcXRxVVFh0bCU4zJSAsdGB8MidCFEVBE1NLGzEQXTYeXl5fURU8YWVpAwFJEjFUA1o=*

The second string is pretty obvious: 
*123abc456wixandmix*
 
Reffering to the title once again, we need to xor those two strings and we get : 
**working with darlene is so priceless , lets catch WHITEROSE! pwd:3z_t0_foll0w_UP_th1s_0n3**

[Script](/BLACK^YELLOW/solve.py)

Nice! We got first password. Extracting the zip inflates two files: another password protected zip file [part2.zip](/BLACK^YELLOW/part2.zip) and a wav file (I couldn't upload because it's too big) elliot.wav.

After several attempts, i used a [script](/BLACK^YELLOW/solver.py) I've found on github for audio steganography
https://gist.github.com/sumit-code/5c91613fc6a20931dcad933e105e80e8#file-audio-steganography-receiver-py

And we get:
**Sucessfully decoded: Old trick hidding message in a song -Darlene , go on ! pwd:W3_d0m1naTe_h3r3**

Using that password we extract the last file [scy_11.png](/BLACK^YELLOW/scy_11.png) . Running file command on that file reveals it's not an Image but: *scy_11.png: UTF-8 Unicode text*

The text was: **A·iobend}fws··t3o·th·?!s_3·eik··{Ds·rtiGSW4n··eloe3rt·arlocLl_·loeduL3f·lsd·r_na··e·jid3i·,·non0_l·**

The name of the file itself was the solution for this cipher. It's *Scytale Cipher* with **11** turns of Band. Few quick clicks on dcode.fr and we had our flag!

![](/BLACK^YELLOW/flag.png)

**Flag: Securinets{W3LL_d0n3_D4rl3n3_do3snt_fail}**
