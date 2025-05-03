# slicing = creates a substring by extracting elements from another string 
# indexing or slice
# [start:step:stop] -- here start is inclusive, step is exclusive (so +1), stop is 

name = "Bro Code"
firstName = name[0:3] #short hand is :3 (automatically gets the first)
secondName = name[4:8] # short hand is 4: (automatically gets the last)
funkyName = name[:8:3] # grab every x character after including the first 
reverseName = name[::-1]
 
print(firstName) # prints Bro
print(secondName) # prints Code
print(reverseName)


# slicing 

website = "https://www.bing.com/"
company = slice(12,-5)
print(website[company])