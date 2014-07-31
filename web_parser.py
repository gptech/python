import re
from urllib2 import urlopen

myAddress = "http://RealPython.com/practice/dionysus.html"

htmlPage = urlopen(myAddress)

htmlText = htmlPage.read()

#name the strings that you want to begin from

Name = "Name: "

Color = "Color: "


# To use the string.find function effectively, tell it to look for the string given in the argument
# IE htmlText.find(Name) and then use the + to tell find to anchor itself after you reach the end of the matching string.
# This sets your starting point for when you want to parse between data.
xstart = htmlText.find(Name) + len(Name)

# Here we tell the string.find method to look for this string in the arguement.
# For the purpose of this, xend is just going to be where are parse will stop
# at the first charcter which would be this end of the header tag.
xend = htmlText.find("</h2>")



#Exact same setup as described above.

ystart = htmlText.find(Color) + len(Color)
yend = htmlText.find("</center>")

# So here we reference our start and end points respectively.
# Tell print to print out the range between our start and end points which
# would give use the exact text we want to standard output.

print htmlText[xstart:xend], htmlText[ystart:yend]

#Here we use the regular expression to find the string we want pretty easily
reresult1 = re.findall("Name:.Dionysus", htmlText)
reresult2 = re.findall("Favorite.Color:", htmlText)


# Since it gets returned as a list, join all the whitespace and make it a sptring and then split that up based on whitespace
stringreresult1 = ' '.join(reresult1)
splitstringreresult1 = stringreresult1.split(None)

#same as above
stringreresult2 = ' '.join(reresult2)
splitstringreresult2 = stringreresult2.split(None)


#Print the split strings into lists
print splitstringreresult1[1], splitstringreresult2